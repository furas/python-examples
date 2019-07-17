#!/usr/bin/env python

# date: 2019.07.07
# https://stackoverflow.com/questions/56924111/roll-up-image-implementation-using-canvas-python

import tkinter as tk
from PIL import Image, ImageTk


def scroll_image():
    global offset_y  # inform function that you want to assign value to external variable instead of local one.

    # move image
    canvas.move(img_id, offset_x, offset_y)
    
    # get current position
    x, y = canvas.coords(img_id)
    print(x, y)

    # set position (if you don't use canvas.move)
    #canvas.coords(img_id, x+offset_x, y+offset_y)
    # x += offset_x
    # y += offset_y

    # change direction
    if y <= -100 or y >= 0:
        offset_y = -offset_y

    # repeat after 20ms
    root.after(20, scroll_image)


offset_x = 0
offset_y = -3

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack(fill='both', expand=True) # use full window

#photo = tk.PhotoImage(file="Capture.gif")
image = Image.open("image.jpg")
photo = ImageTk.PhotoImage(image)
img_id = canvas.create_image(0, 0, image=photo)

# start scrolling
scroll_image()

root.mainloop()

