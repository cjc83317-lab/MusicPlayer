import os
import vlc
import tkinter as tk
from tkinter import filedialog, Label

playlist = []
current_index = -1
player = vlc.MediaPlayer()

def play_track(index):
    global current_index
    if 0 <= index < len(playlist):
        current_index = index
        media = vlc.Media(playlist[index])
        player.set_media(media)
        player.play()
        status_label.config(text=f"Playing: {os.path.basename(playlist[index])}")

def pause_track():
    player.pause()
    status_label.config(text="Paused")

def stop_track():
    player.stop()
    status_label.config(text="Stopped")

def next_track():
    global current_index
    if current_index + 1 < len(playlist):
        play_track(current_index + 1)

def previous_track():
    global current_index
    if current_index > 0:
        play_track(current_index - 1)

def choose_files():
    global playlist
    files = filedialog.askopenfilenames(
        title="Select audio files",
        filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.flac")]
    )
    if files:
        playlist = list(files)
        play_track(0)

# GUI setup
root = tk.Tk()
root.title("Python 3.14 VLC Music Player")
root.geometry("400x250")

tk.Button(root, text="Choose Files", command=choose_files).pack(pady=5)
tk.Button(root, text="Play", command=lambda: play_track(current_index)).pack(pady=5)
tk.Button(root, text="Pause", command=pause_track).pack(pady=5)
tk.Button(root, text="Stop", command=stop_track).pack(pady=5)
tk.Button(root, text="Previous", command=previous_track).pack(pady=5)
tk.Button(root, text="Next", command=next_track).pack(pady=5)

status_label = Label(root, text="No track playing")
status_label.pack(pady=10)

root.mainloop()