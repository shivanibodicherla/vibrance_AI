# -*- coding: utf-8 -*-
"""
Created on Thu May 16 13:25:51 2024

@author: shiva
"""

import tkinter as tk
from tkinter import messagebox
import requests

def fetch_lyrics():
    song_title = song_entry.get().strip()
    artist_name = artist_entry.get().strip()

    if not song_title or not artist_name:
        messagebox.showerror("Error", "Please enter both song title and artist name.")
        return

    try:
        # Fetch lyrics using Lyrics.ovh API
        response = requests.get(f"https://api.lyrics.ovh/v1/{artist_name}/{song_title}")
        data = response.json()

        if "lyrics" in data:
            lyrics = data["lyrics"]
            lyrics_text.config(state="normal")
            lyrics_text.delete('1.0', tk.END)
            lyrics_text.insert(tk.END, lyrics)
            lyrics_text.config(state="disabled")
        else:
            messagebox.showerror("Error", "Lyrics not found for the provided song and artist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Song Lyrics Extractor")
root.configure(bg="black")

# Create labels and entry fields
song_label = tk.Label(root, text="Song Title:", bg="black", fg="white")
song_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
song_entry = tk.Entry(root)
song_entry.grid(row=0, column=1, padx=10, pady=5)

artist_label = tk.Label(root, text="Artist Name:", bg="black", fg="white")
artist_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
artist_entry = tk.Entry(root)
artist_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a button to fetch lyrics
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a text widget to display lyrics
lyrics_text = tk.Text(root, height=20, width=60, bg="black", fg="white")
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
lyrics_text.config(state="disabled")

# Center the window
window_width = 400
window_height = 450
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Start the GUI event loop
root.mainloop()
