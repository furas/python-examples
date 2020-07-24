#!/usr/bin/env python3

import tkinter as tk
from PIL import ImageTk #,Image        

root = tk.Tk()

#image = ImageTk.PhotoImage(Image.open("square-rotated.png"))
image = ImageTk.PhotoImage(file="square-rotated.png")

tk.Label(root, image=image, bg='green').pack()
tk.Label(root, image=image, bg='blue').pack()
tk.Label(root, image=image, bg='yellow').pack()

w = image.width()
h = image.height()

c = tk.Canvas(root, width=w*2, height=h, bg='black')
c.pack()

c.create_image((w-(w//2), h//2), image=image)
c.create_image((w       , h//2), image=image)
c.create_image((w+(w//2), h//2), image=image)

root.mainloop()   
