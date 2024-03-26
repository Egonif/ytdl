#!/bin/bash

OS="`uname`"
case $OS in
  'Linux')
    sudo apt install yt-dlp ffmpeg -y
    ;;
  'WindowsNT')
    ;;
  'Darwin') 
    # Homebrew installation
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    # Packages installation
    brew install yt-dlp ffmpeg
    ;;
  *) ;;
esac
