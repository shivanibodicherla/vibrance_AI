# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:16:43 2024

@author: shiva
"""

import tkinter as tk
from tkinter import scrolledtext, filedialog
from PIL import Image, ImageTk
import google.generativeai as genai
import requests
from io import BytesIO

# Replace the API_KEY string with your actual API key
API_KEY = "AIzaSyDoj5c3b3Vlp8MOXlQjmj8MP7yPK8Lu_Ns"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

def generate_response():
    user_input = user_input_entry.get("1.0", tk.END).strip()
    if user_input.lower() == "exit":
        root.destroy()
    else:
        response = model.generate_content(user_input)
        display_text("User", user_input, "user")
        if 'image' in user_input.lower():
            image_url = extract_image_url(response.text)
            if image_url:
                display_image(image_url)
        else:
            display_text("Chinna", response.text, "bot")
        user_input_entry.delete("1.0", tk.END)

def extract_image_url(response_text):
    # Dummy function to extract image URL from the response text
    # Replace with actual logic to parse the response and get the image URL
    # For demonstration purposes, let's assume the response contains a URL directly
    return response_text.strip()

def display_text(sender, text, tag):
    response_text.config(state=tk.NORMAL)
    response_text.insert(tk.END, f"{sender}: {text}\n", tag)
    response_text.config(state=tk.DISABLED)

def display_image(url):
    try:
        response = requests.get(url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img.thumbnail((400, 400))  # Resize image to fit in the chat window
        img_tk = ImageTk.PhotoImage(img)

        response_text.config(state=tk.NORMAL)
        response_text.image_create(tk.END, image=img_tk)
        response_text.insert(tk.END, "\n\n")  # Add some space after the image
        response_text.image = img_tk  # Keep a reference to the image
        response_text.config(state=tk.DISABLED)
    except Exception as e:
        display_text("Error", "Failed to load image.", "error")

# Create the main window
root = tk.Tk()
root.title("Generative AI Chat")
root.geometry("800x600")
root.configure(bg="#f5f5f5")

# Create a frame for the chat history
chat_frame = tk.Frame(root, bg="#f5f5f5")
chat_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create a scrolled text widget for displaying the conversation
response_text = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12), bg="#ffffff", fg="#000000", padx=10, pady=10)
response_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
response_text.tag_config("user", foreground="blue")
response_text.tag_config("bot", foreground="green")
response_text.tag_config("error", foreground="red")

# Create a frame for the user input
input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(pady=10, padx=10, fill=tk.X)

# Create a text widget for user input
user_input_entry = tk.Text(input_frame, height=3, font=("Arial", 12), bg="#ffffff", fg="#000000", padx=10, pady=10)
user_input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

# Create a button to send the prompt
send_button = tk.Button(input_frame, text="Send", command=generate_response, bg="#4CAF50", fg="#ffffff", font=("Arial", 12), padx=20, pady=10)
send_button.pack(side=tk.RIGHT)

# Run the application
root.mainloop()
