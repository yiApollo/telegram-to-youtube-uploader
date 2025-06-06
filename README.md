# telegram-to-youtube-uploader
A program that downloads videos from Telegram channels and automatically uploads them to YouTube as unlisted, organizing them into playlists based on the filenames.

# 📥 Telegram to YouTube Uploader

Automates downloading videos from **Telegram channels** (like online courses), organizing them locally, and uploading them to **YouTube** as **unlisted videos** in a private playlist with proper naming and order.

---
![MIT License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10+-blue)


## 🔧 Features

* Connects to your **Telegram account**
* Lists all **joined channels** with their **IDs**
* Downloads **videos** from a selected channel
* Saves videos to the `downloads/` folder with names like:

  * `Lesson 1 - ChannelName.mp4`
  * `Lesson 2 - ChannelName.mp4`
* You manually upload videos to YouTube
* Then the script:

  * Creates an **unlisted playlist**
  * Names it after the original **Telegram channel**
  * Adds videos in order (`Lesson 1 → Lesson 2`)

---

## ⚠️ Why Not Use API for Upload?

Due to YouTube Data API limitations:

* **Uploads via API (free)**: limited to **6 videos/day**
* **Playlist management via API**: allows **100+ videos/day**

**We only use the API to organize videos — not to upload them.**

---

## 🚀 How to Use

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Download videos from Telegram

```bash
python3 main.py
```

* Lists your channels
* Ask for the channel ID
* Saves videos to `downloads/` with proper naming

##### Remember
Go to My Telegram, API Development Tools, and create an API.


### 3. Upload videos manually to YouTube

* Upload all videos from `downloads/`

### 4. Organize uploaded videos on YouTube

```bash
python3 organizer.py
```

* Creates an unlisted playlist
* Adds videos using filenames (Lesson 1, 2, etc.)

---

### 5. AI Summarization

Use [YouTube Transcript Extractor](https://github.com/yiApollo/YouTube-Transcript-Extractor-Auto-Whisper-Fallback)

Simply upload the complete `.md` file with full playlist transcripts—or only the specific `.md` files you need—to Google NotebookLM, ChatGPT, or your preferred AI, and ask for a summary.

This tool wasn't built for summarizing individual videos—there are already many tools for that. It was designed specifically to help summarize entire playlists of content and courses from YouTube.


---

## ✅ Requirements

* **Telegram API credentials**: [my.telegram.org](https://my.telegram.org)
* **Google Cloud project** with YouTube Data API enabled
* `credentials/client_secret.json` file

---

## 🛠️ Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/telegram-to-youtube.git
cd telegram-to-youtube
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set Up Telegram API

* Go to [my.telegram.org](https://my.telegram.org)
* Login with your phone number
* Under **API Development Tools**, create a new app
* Get your `api_id` and `api_hash`
* Edit `telegram_config.py` with those values:

```python
API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
```

### 3. Enable YouTube Data API (Google Cloud)

* Go to: [console.cloud.google.com](https://console.cloud.google.com)
* Create a new project
* Enable: **YouTube Data API v3**
* Create credentials:

  * Type: **OAuth Client ID**
  * App type: **Desktop App**
* Download JSON → save as `credentials/client_secret.json`

### 4. Add Test User

* Go to: OAuth Consent Screen
* Set user type to **External**
* Add your Google email under **Test Users**

### 5. First-Time Authentication

* Run any script (e.g. `organizer.py`)
* Browser will open for login/authorization
* Paste code back into terminal
* Token is saved automatically
A program that downloads videos from Telegram channels and automatically uploads them to YouTube as unlisted, organizing them into playlists based on the filenames.

---

## 📌 Quick Usage Recap

```bash
# Step 1 – Download Telegram videos
python3 main.py

# Step 2 – Manually upload to YouTube
# → Set all as "Unlisted"

# Step 3 – Organize playlist
python3 organizador.py
```
---

## ⚠️ Caution

The YouTube organizer script relies on **exact video titles** to work correctly. It only processes videos with titles in the following format:

```text
Lesson 1
Lesson 2
```

If your videos do not follow this format, they will be ignored.

To ensure proper detection and organization:

    Upload your videos with titles like Lesson 1, Lesson 2, etc.

    The script will automatically rename them to:

Lesson 1 - ChannelName

And include them in the playlist.


## 📜 License
MIT — feel free to use, modify, and share.

---

# ⚡ Powerful Usage: Automate Uploads & Summarize Entire Playlists

Use with [YouTube Transcript Extractor](https://github.com/yiApollo/YouTube-Transcript-Extractor-Auto-Whisper-Fallback)
to summarize your content.
