#!/usr/bin/env python3

import tkinter as tk
from PIL import Image, ImageTk

# --- functions ---

def on_click(event=None):
    # `command=` calls function without argument (so I set event=None)
    # `bind` calls function with one argument
    if event:
        print("Label clicked (x,y:", event.x, event.y, ')')
    else:
        print("Button clicked")

# --- main ---
    
# init    
root = tk.Tk()

# load image
image = Image.open("/home/furas/Obrazy/test.png")
photo = ImageTk.PhotoImage(image)

# label with image
l = tk.Label(root, image=photo)
l.pack()

# bind click event to image
l.bind('<Button-1>', on_click)

# button with image binded to the same function 
b = tk.Button(root, image=photo, command=on_click)
b.pack()

# button with text closing window
b = tk.Button(root, text="Close", command=root.destroy)
b.pack()
    
# "start the engine"
root.mainloop()
