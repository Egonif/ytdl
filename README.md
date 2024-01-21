# YTDL

Here's a repository where you can download the latest yt-dlp updates for downloading YouTube videos.

## Installation

### MacOS

Install Homebrew (package manager):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Follow the instructions at the end of the order.

Install yt-dlp and ffmpeg
```bash
brew install yt-dlp ffmpeg
```

### Windows

Install Chocolatey (package manager) with PowerShell:

You must ensure Get-ExecutionPolicy is not Restricted:
```powershell
Set-ExecutionPolicy AllSigned
```

Then install Chocolatey:
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Finally, use Chocolatey to install yt-dlp and ffmpeg:
```powershell
choco install yt-dlp ffmpeg
```

## Usage

There are differents options for yt-dlp, but here's some examples:
```bash
# Download the best video in mp4
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" -o "%(title)s.%(ext)s" [YOUR LINK HERE]
```

```bash
# Download mp3 audio
yt-dlp -o "%(title)s.%(ext)s" -x --audio-format mp3 [YOUR LINK HERE]
```
