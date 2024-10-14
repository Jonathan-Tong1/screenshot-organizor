import os
import tkinter as tk
from tkinter import filedialog, messagebox

def set_screenshot_location(folder_path):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Set the screenshot location using the correct command
    os.system(f'defaults write com.apple.screencapture location "{folder_path}"')
    os.system('killall SystemUIServer')  # Refresh the System UI

    messagebox.showinfo("Success", f'Screenshot location set to: {folder_path}')

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        set_screenshot_location(folder_path)


# Create GUI

root = tk.Tk()
root.title("Screenshot Location Setter")

label = tk.Label(root, text="Set your screenshot folder:")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=10)

root.mainloop()
