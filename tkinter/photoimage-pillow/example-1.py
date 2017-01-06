#!/usr/bin/env python3

import tkinter as tk
from PIL import ImageTk, Image

# --- change image ---

img1 = Image.open("ball-01.png")

img2 = img1.convert("RGBA")

pixdata = img2.load()

for y in range(img2.size[1]):
    for x in range(img2.size[0]):
        if pixdata[x, y][:3] == (255, 0, 0):
            pixdata[x, y] = (255, 255, 255, 0)

# --- main ---

root = tk.Tk()

photo1 = ImageTk.PhotoImage(img1)
panel = tk.Label(root, image=photo1)
panel.pack()

photo2 = ImageTk.PhotoImage(img2)
panel = tk.Label(root, image=photo2)
panel.pack()

root.mainloop()
