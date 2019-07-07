#!/usr/bin/env python3

import tkinter as tk


# --- constants --- (UPPER_CASE names)

# window/canvas size
SCREEN_WIDTH  = 400
SCREEN_HEIGHT = 300

# --- functions --- (lower_case names)

def move_old():
    global speed_x
    global speed_y
    
    # get position
    (x1, y1, x2, y2) = canvas.coords(ball)

    # move
    x1 += speed_x
    x2 += speed_x
    y1 += speed_y
    y2 += speed_y

    # set position
    canvas.coords(ball, x1, y1, x2, y2)
    
    # change direction
    if x1 <= 0 or x2 >= SCREEN_WIDTH:
        speed_x = -speed_x
    if y1 <= 0 or y2 >= SCREEN_HEIGHT:
        speed_y = -speed_y

    # run again after 30ms
    root.after(30, move)


def move():
    global speed_x
    global speed_y
    
    # move
    canvas.move(ball, speed_x, speed_y)

    # get position
    (x1, y1, x2, y2) = canvas.coords(ball)
    
    # change direction
    if x1 <= 0 or x2 >= SCREEN_WIDTH:
        speed_x = -speed_x
    if y1 <= 0 or y2 >= SCREEN_HEIGHT:
        speed_y = -speed_y

    # run again after 30ms
    root.after(30, move)

# --- main --- (lower_case names)

# ball speed
speed_x = 10
speed_y = 10

root = tk.Tk()
root.geometry('{}x{}'.format(SCREEN_WIDTH, SCREEN_HEIGHT))

canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

ball = canvas.create_oval([0, 0, 30, 30], fill='black')
move()

root.mainloop()

