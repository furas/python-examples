#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def move(diff_x, diff_y):
    global centerx
    global centery
    
    for item in items:
        canvas.move(item, diff_x, diff_y)

    centerx += diff_x
    centery += diff_y

    for item in lines:
        x1, y1, x2, y2 = canvas.coords(item)
        canvas.coords(item, x1, y1, centerx, centery)

def move_item(event):
    global old_x
    global old_y
    diff_x = event.x - old_x
    diff_y = event.y - old_y
    move(diff_x, diff_y)
    old_x = event.x
    old_y = event.y
        
def move_horizontal(event):
    global old_x
    diff_x = event.x - old_x
    move(diff_x, 0)
    old_x = event.x

def move_vertical(event):
    global old_y
    diff_y = event.y - old_y
    move(0, diff_y)
    old_y = event.y

def save_position(event):
    global old_x
    global old_y    
    old_x = event.x
    old_y = event.y
    
def create_objects(event=None):
    global centerx
    global centery
    global lines
    global items
    
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    centerx = w//2
    centery = h//2
    
    lines = [
        canvas.create_line(0, 0, centerx, centery),
        canvas.create_line(0, h, centerx, centery),
        canvas.create_line(w, 0, centerx, centery),
        canvas.create_line(w, h, centerx, centery),
    ]

    # create objects
    items = [
        canvas.create_rectangle(centerx-50, centery-50, centerx-100, centery-100, fill='red'),
        canvas.create_rectangle(centerx-50, centery+50, centerx-100, centery+100, fill='blue'),
        canvas.create_rectangle(centerx+50, centery-50, centerx+100, centery-100, fill='yellow'),
        canvas.create_rectangle(centerx+50, centery+50, centerx+100, centery+100, fill='green'),
    ]
    
        
# --- main ---

old_x = 0
old_y = 0

root = tk.Tk()


canvas = tk.Canvas(root, width=500, height=300, bg='gray')
canvas.pack(fill='both', expand=True)

canvas.bind("<Button-1>", save_position)
canvas.bind("<B1-Motion>", move_item)
canvas.bind("<Shift-B1-Motion>", move_horizontal)
canvas.bind("<Control-B1-Motion>", move_vertical)

root.after(100, create_objects) # run later so `tkinter` will already know window size

root.mainloop()
