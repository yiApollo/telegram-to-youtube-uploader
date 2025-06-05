import os
import re
from googleapiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow

CLIENT_SECRET_FILE = 'credentials/client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube']

# Authenticate and return the YouTube API client
def auth_youtube():
    storage = Storage('youtube-oauth2.json')
    creds = storage.get()
    if not creds or creds.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        creds = run_flow(flow, storage)
    return build('youtube', 'v3', credentials=creds)

# Create an unlisted playlist with a custom name and optional description
def criar_playlist(youtube, playlist_name, description):
    response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": playlist_name,
                "description": description,
            },
            "status": {
                "privacyStatus": "unlisted"
            }
        }
    ).execute()
    return response["id"]

# Retrieve all videos with titles like "Lesson X"
def listar_videos_do_canal(youtube):
    videos = []
    request = youtube.search().list(
        part="snippet",
        forMine=True,
        type="video",
        maxResults=50
    )
    while request:
        response = request.execute()
        for item in response["items"]:
            title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            if re.match(r"Lesson\s+\d+$", title.strip()):
                videos.append((title, video_id))
        request = youtube.search().list_next(request, response)
    return videos

# Main routine: update titles, set privacy, and add videos to playlist
def organizar():
    youtube = auth_youtube()
    channel_name = input("Channel name (used for titles and playlist name): ")

    playlist_description = input("Playlist description (press Enter to leave empty): ").strip()
    if not playlist_description:
        playlist_description = ""

    playlist_id = criar_playlist(youtube, channel_name, playlist_description)

    videos = listar_videos_do_canal(youtube)

    # Extract lesson number from title
    def extract_num(title):
        return int(re.search(r"Lesson\s+(\d+)", title).group(1))

    videos_sorted = sorted(videos, key=lambda x: extract_num(x[0]))

    for i, (old_title, video_id) in enumerate(videos_sorted, start=1):
        new_title = f"Lesson {i} - {channel_name}"
        description = f"Lesson {i} imported from Telegram channel: {channel_name}"

        # Update title, description, and privacy
        youtube.videos().update(
            part="snippet,status",
            body={
                "id": video_id,
                "snippet": {
                    "title": new_title,
                    "description": description,
                    "categoryId": "22"
                },
                "status": {
                    "privacyStatus": "unlisted"
                }
            }
        ).execute()
        print(f"📝 Updated: {new_title}")

        # Add to playlist
        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        ).execute()
        print(f"➕ Added to playlist: {video_id}")

if __name__ == "__main__":
    organizar()

