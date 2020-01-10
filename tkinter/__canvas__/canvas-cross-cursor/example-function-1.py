#!/usr/bin/env python3 

# date: 2020.01.04
# 

import tkinter as tk

# --- functions ---

def on_move(event):
    x = event.x
    y = event.y
    canvas.coords(cursorx, x, 0, x, root.winfo_height())
    canvas.coords(cursory, 0, y, root.winfo_width(), y)

# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

cursorx = canvas.create_line(0, 0, 0, root.winfo_height())
cursory = canvas.create_line(0, 0, root.winfo_width(), 0)

canvas.bind('<Motion>', on_move)

root.mainloop()

