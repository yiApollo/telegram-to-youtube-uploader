from telethon.sync import TelegramClient
from tqdm import tqdm
import os

API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'
SESSION_NAME = 'telegram_session'

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

def list_channels():
    client.start()
    print("Available channels:")
    for dialog in client.get_dialogs():
        if dialog.is_channel:
            print(f"ID: {dialog.entity.id} | Name: {dialog.name}")

def download_videos_by_id(channel_id):
    os.makedirs("downloads", exist_ok=True)
    client.start()
    entity = client.get_entity(channel_id)

    existing_files = set(os.listdir("downloads/"))
    counter = 1

    for msg in client.iter_messages(entity, reverse=True):
        if msg.video:
            filename = f"Lesson {counter}.mp4"
            path = f"downloads/{filename}"

            if filename in existing_files:
                print(f"🟡 Already exists: {filename}")
            else:
                try:
                    print(f"⬇️  Downloading: {filename}")
                    with tqdm(total=100, desc="Progress", bar_format="{l_bar}{bar}| {n_fmt}%") as pbar:
                        def progress(current, total):
                            percent = int(current * 100 / total)
                            pbar.n = percent
                            pbar.refresh()

                        client.download_media(msg, file=path, progress_callback=progress)

                    print(f"✅ Downloaded: {filename}")
                except Exception as e:
                    print(f"❌ Failed to download {filename}: {e}")
            counter += 1

