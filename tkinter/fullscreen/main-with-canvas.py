#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_escape(event=None):
    print("escaped")
    root.destroy()

# --- main ---

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# --- fullscreen ---

#root.overrideredirect(True)  # sometimes it is needed to toggle fullscreen
                              # but then window doesn't get events from system
#root.overrideredirect(False) # 

root.attributes("-fullscreen", True) # run fullscreen
root.wm_attributes("-topmost", True) # keep on top
#root.focus_set() # set focus on window

# --- closing methods ---

# close window with key `ESC`
root.bind("<Escape>", on_escape)

# close window after 5s if `ESC` will not work
root.after(5000, root.destroy) 

# --- canvas ---

canvas = tk.Canvas(root)
canvas.pack(fill='both', expand=True)

canvas.create_oval((0, 0, screen_width, screen_height), fill='red', outline='')

# --- start ---

root.mainloop()
