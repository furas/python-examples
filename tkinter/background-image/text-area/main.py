#!/usr/bin/env python3

import tkinter as tk
from PIL import ImageTk

# --- functions ---

def run():
    # all `global` always at the top of function
    # to make it more readable
    global root
    global text

    root = tk.Tk()
    
    image = ImageTk.PhotoImage(file='image.jpg')

    label = tk.Label(root, image=image)
    label.pack(fill='both', expand=True)

    label.image = image # keep reference
    # see Note on http://effbot.org/tkinterbook/photoimage.htm
    
    # Text need `label` as parent
    # `padx`, `pady` create margin so you can see background
    text = tk.Text(label)
    text.pack(fill='both', expand=True, padx=100, pady=100)

    text.insert('end', 'Hello World')    
    
    root.mainloop()

# --- main ---

run()
