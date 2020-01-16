#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def move_item(event):
    global old_x
    global old_y    
    diff_x = event.x - old_x
    diff_y = event.y - old_y
    for item in items:
        canvas.move(item, diff_x, diff_y)
    old_x = event.x
    old_y = event.y

def move_horizontal(event):
    global old_x
    diff_x = event.x - old_x
    for item in items:
        canvas.move(item, diff_x, 0)
    old_x = event.x

def move_vertical(event):
    global old_y
    diff_y = event.y - old_y
    for item in items:
        canvas.move(item, 0, diff_y)
    old_y = event.y

def save_position(event):
    global old_x
    global old_y    
    old_x = event.x
    old_y = event.y
    
# --- main ---

old_x = 0
old_y = 0
# init
root = tk.Tk()

# create canvas
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# create objects
items = [
    canvas.create_rectangle(100, 100, 130, 130, fill='red'),
    canvas.create_rectangle(200, 100, 230, 130, fill='blue'),
    canvas.create_rectangle(100, 200, 130, 230, fill='yellow'),
]

canvas.bind("<Button-1>", save_position)
canvas.bind("<B1-Motion>", move_item)
canvas.bind("<Shift-B1-Motion>", move_horizontal)
canvas.bind("<Control-B1-Motion>", move_vertical)
# start program
root.mainloop()

