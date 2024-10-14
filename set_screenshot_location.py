import os
import tkinter as tk
from tkinter import filedialog, messagebox

def set_screenshot_location(folder_path):
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    os.system(f'defaults location "{folder_path}"')
    messagebox.showinfo("Success", f'Screenshot location set to: {folder_path}')

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        set_screenshot_location(folder_path)


root = tk.Tk()
root.title("Screenshot Location Setter")

label = tk.Label(root, text="Set your screenshot folder:")
label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=10)

root.mainloop()
