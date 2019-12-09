#!/usr/bin/env python3 

# date: 2019.12.07

import tkinter as tk

# --- functions ---

def on_move(event):
    canvas.itemconfigure(text_id, text="({}, {})".format(event.x, event.y))

# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()
canvas.bind("<Motion>", on_move)

text_id = canvas.create_text(10, 10, text="(?, ?)", anchor="nw")  

root.mainloop()
