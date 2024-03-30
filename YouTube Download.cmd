@echo off
setlocal enabledelayedexpansion

set /p "url=Entrer le lien de la vidéo: "
set /p "format=Entrer le format de la vidéo (mp3/mp4): "
set "browseforfolder="(new-object -COM 'Shell.Application').BrowseForFolder(0,'Please choose a folder',0,0).self.path""
for /f "usebackq delims=" %%I in (`powershell %browseforfolder%`) do set "destinationfolder=%%I"

if "%format%"=="mp3" (
    @REM Download mp3
    yt-dlp -o "!destinationfolder!\%%(title)s.%%(ext)s" -x --audio-format mp3 %url%
)
if "%format%"=="mp4" (
    @REM Download mp4
    yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" -o "!destinationfolder!\%%(title)s.%%(ext)s" %url%
)