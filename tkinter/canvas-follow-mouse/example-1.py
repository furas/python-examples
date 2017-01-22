#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def move_a(event):
    canvas.coords(a, event.x-50, event.y-50, event.x+50, event.y+50)

def move_b():
    # inform function to use external/global variable
    # because we use `=` to change its value
    global b_speed_x
    global b_speed_y
    global b_direction

    canvas.move(b, b_speed_x, b_speed_y)

    # get current position
    x1, y1, x2, y2 = canvas.coords(b)

    if b_direction == 'down':
        if y2 >= 300:
            b_direction = 'right'
            b_speed_x = 5
            b_speed_y = 0
    elif b_direction == 'up':
        if y1 <= 0:
            b_direction = 'left'
            b_speed_x = -5
            b_speed_y = 0
    elif b_direction == 'right':
        if x2 >= 500:
            b_direction = 'up'
            b_speed_x = 0
            b_speed_y = -5
    elif b_direction == 'left':
        if x1 <= 0:
            b_direction = 'down'
            b_speed_x = 0
            b_speed_y = 5

    # move again after 25 ms (0.025s)
    root.after(25, move_b)

# --- main ---

# init
root = tk.Tk()

# create canvas
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# create objects
a = canvas.create_rectangle(0, 0, 100, 100, fill='red')
b = canvas.create_rectangle(0, 0, 100, 100, fill='blue')
# create global variables
b_direction = 'down'
b_speed_x = 0
b_speed_y = 5

# start moving `a` with mouse
canvas.bind("<Motion>", move_a)

# start moving `b` automatically
move_b()

# start program
root.mainloop()
