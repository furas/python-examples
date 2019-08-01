#!/usr/bin/env python3

# date: 2019.08.01
# 

import tkinter as tk
import random

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 200

DISTANCE = 50
NUMBER = (SCREEN_WIDTH // DISTANCE) + 1

# --- functions --- (lower_case names)

def move():
    # remove first
    data.pop(0)

    # add last
    data.append(random.randint(0,SCREEN_HEIGHT))
    
    # remove all lines
    canvas.delete('all')
    
    # draw new lines
    for x, (y1, y2) in enumerate(zip(data, data[1:])):
        x1 = x * DISTANCE
        x2 = (x+1) * DISTANCE  # x1 + DISTANCE
        canvas.create_line([x1, y1, x2, y2])
    
    # run again after 500ms
    root.after(500, move)

def draw_data():

# --- main --- (lower_case names)

# data at start
data = [random.randint(0, SCREEN_HEIGHT) for _ in range(NUMBER)]


root = tk.Tk()
root.geometry('{}x{}'.format(SCREEN_WIDTH, SCREEN_HEIGHT))

canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

# start animation    
move()

root.mainloop()

