# YTDL

> New update soon !

Here's a repository where you can download the latest yt-dlp updates for downloading YouTube videos.

# Installation

## MacOS

Install Homebrew (package manager):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the instructions at the end of the order.

Install yt-dlp and ffmpeg

```bash
brew install yt-dlp ffmpeg
```

## Windows

Open Cmd in Administrator Mode

```powershell
curl -s --location --request GET https://raw.githubusercontent.com/Egonif/ytdl/main/install.cmd --output %TEMP%\install.cmd && %TEMP%\install.cmd
```

# Usage

There are differents options for yt-dlp, but here's some examples:

```bash
# Download the best video in mp4
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" -o "%(title)s.%(ext)s" [YOUR LINK HERE]

# Download best video in mp4 for mac user (compatibility with QuickTime Player)
yt-dlp -S "+codec:h264" -o "%(title)s.%(ext)s" [YOUR LINK HERE]

# Download mp3 audio
yt-dlp -o "%(title)s.%(ext)s" -x --audio-format mp3 [YOUR LINK HERE]

# Download all the playlist's audios in mp3
yt-dlp -o "%(title)s.%(ext)s" -x --audio-format mp3 --yes-playlist --playlist-items [NUMBER IN PLAYLIST] [YOUR LINK HERE]

# Download all the playlist's videos in mp4
yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' -o "%(title)s.%(ext)s" --yes-playlist --playlist-items [NUMBER IN PLAYLIST] [YOUR LINK HERE]
```
