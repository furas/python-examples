#!/usr/bin/env python3

import tkinter as tk

# --- constants --- (UPPER_CASE names)

DISPLAY_WIDHT = 800
DISPLAY_HEIGHT = 600

CENTER_X = DISPLAY_WIDHT//2
CENTER_Y = DISPLAY_HEIGHT//2

# --- functions --- (lower_case names)

def move():

    # don't move if gama paused
    if key_up:
        canvas.move(a, 0, -5)
    elif key_down:
        canvas.move(a, 0, 5)

    # get current position
    x1, y1, x2, y2 = canvas.coords(a)

    if x2 > DISPLAY_WIDHT:
        canvas.move(a, a_speed_x, DISPLAY_WIDHT-x2)
    if x1 < 0:
        canvas.move(a, a_speed_x, DISPLAY_WIDHT-x1)

    # move again after 25 ms (0.025s)
    root.after(25, move)

def up_press(event):
    key_up = True
    print('press')


def up_release(event):
    global key_up
    key_up = False
    print('release')

# --- main --- (lower_case names)

# init
root = tk.Tk()

# create canvas
canvas = tk.Canvas(root, width=DISPLAY_WIDHT, height=DISPLAY_HEIGHT)
canvas.pack()

# create objects
a = canvas.create_rectangle(CENTER_X-10, CENTER_Y-10, CENTER_X+10, CENTER_Y+10, fill='red')
a_speed_x = 0
a_speed_y = 0

# start moving `a` with mouse
key_up = False
key_down = False
root.bind("<Up>", up_press)
root.bind("<KeyRelease-Up>", up_release)

move()

# start program
root.mainloop()
