#!/usr/bin/env python3

import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, heigh=300)
canvas.pack()

img = Image.open('sun.png')
photo = ImageTk.PhotoImage(img)
canvas.create_image((150, 150), image=photo)

root.mainloop()
