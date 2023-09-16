#!/usr/local/bin/python3

from tkinter import filedialog
import os
import subprocess
import tkinter as tk
import ttkbootstrap as ttk


# functions
def download():
    link    = entry.get()
    format  = entry_format.get()
    dirpath = filedialog.askdirectory()
    entry.delete(first=0, last=len(link))
    os.chdir(dirpath)
    if link != "" and format != "" and dirpath != "":
        if format == "mp4":
            subprocess.call(
                [f'yt-dlp -S "+codec:h264" -o "%(title)s.%(ext)s" "{link}"'], shell=True
            )
        else:
            subprocess.call(
                [f'yt-dlp -o "%(title)s.%(ext)s" -x --audio-format {format} "{link}"'],
                shell=True,
            )
        # End window
        endwindow = ttk.Toplevel(window)
        endwindow.title("Confirmation")
        endwindow.geometry("200x100")
        title_label = ttk.Label(
            master=endwindow, text="Downloaded", font="Helvetica 20"
        )
        buttonclose = ttk.Button(master=endwindow, text="Ok", command=endwindow.destroy)
        title_label.pack(pady=10)
        buttonclose.pack(pady=10)
    else:
        # Error window
        errorwindow = ttk.Toplevel(window)
        errorwindow.title("Error")
        errorwindow.geometry("300x100")
        title_label = ttk.Label(
            master=errorwindow,
            text="Please provide all informations",
            font="Helvetica 15",
        )
        buttonclose = ttk.Button(
            master=errorwindow, text="Ok", command=errorwindow.destroy
        )
        title_label.pack(pady=10)
        buttonclose.pack(pady=10)


# window
window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("400x150")

# title
title_label = ttk.Label(
    master=window, text="YouTube Downloader", font="Helvetica 24 bold"
)
title_label.pack(pady=5)

# input field
input_frame  = ttk.Frame(master=window)
entry        = ttk.Entry(master=input_frame)
format       = tk.StringVar()
entry_format = ttk.Combobox(
    master=input_frame, width=5, textvariable=format, values=["mp4", "wav", "mp3"]
)
button = ttk.Button(master=input_frame, text="Download", command=download)
entry.pack(side="left")
entry_format.pack(side="left")
button.pack(side="right")
input_frame.pack(pady=10)

# # output
# output_string = tk.StringVar()
# output_label = ttk.Label(master=window, font="Helvetica 24", text="")
# output_label.pack(pady=10)

# run
window.mainloop()
