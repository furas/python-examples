#!/usr/bin/env python3

import tkinter as tk
from PIL import Image, ImageTk

# --- function ---

def on_click(event):
    print(event)

def on_click_tag(tag):
    canvas.delete(tag)
    
# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

pil_image = Image.open("/home/furas/Obrazy/inne/hal_50x50.png")
#pil_image = pil_image.resize((1000,1000)) #resize image

photo = ImageTk.PhotoImage(pil_image)
image = canvas.create_image(0, 0, image=photo, anchor="nw")

#canvas.tag_bind(image, '<Button-1>', on_click)
canvas.tag_bind(image, '<Button-1>', lambda event, tag=image:on_click_tag(tag))

root.mainloop()
