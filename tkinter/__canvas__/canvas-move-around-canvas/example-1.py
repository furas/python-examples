#!/usr/bin/env python3

import tkinter as tk

# --- constants --- (UPPER_CASE names)

DISPLAY_WIDHT = 800
DISPLAY_HEIGHT = 600

# --- classes --- (CamelCase names)

#class Player():
#    pass

#class BlueEnemy():
#    pass

# --- functions --- (lower_case names)

def move_a(event):
    # don't move if gama paused
    if not game_paused:
        canvas.coords(a, event.x-50, event.y-50, event.x+50, event.y+50)

def move_b():
    # inform function to use external/global variable
    # because we use `=` to change its value
    global b_speed_x
    global b_speed_y
    global b_direction

    # don't move if gama paused
    if not game_paused:
        canvas.move(b, b_speed_x, b_speed_y)

        # get current position
        x1, y1, x2, y2 = canvas.coords(b)

        if b_direction == 'down':
            if y2 >= DISPLAY_HEIGHT:
                b_direction = 'right'
                b_speed_x = 5
                b_speed_y = 0
        elif b_direction == 'up':
            if y1 <= 0:
                b_direction = 'left'
                b_speed_x = -5
                b_speed_y = 0
        elif b_direction == 'right':
            if x2 >= DISPLAY_WIDHT:
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

def pause(event):
    global game_paused

    # change True/False
    game_paused = not game_paused

    if game_paused:
        # center text on canvas
        canvas.coords(text_pause, DISPLAY_WIDHT//2, DISPLAY_HEIGHT//2)
    else:
        # move text somewhere outside canvas
        canvas.coords(text_pause, -1000, -1000)

# --- main --- (lower_case names)

# init
root = tk.Tk()

# key `p` pause game
game_paused = False
root.bind('p', pause)

# create canvas
canvas = tk.Canvas(root, width=DISPLAY_WIDHT, height=DISPLAY_HEIGHT)
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

# create text somewhere outside canvas - so it will be "invisible"
text_pause = canvas.create_text(-1000, -1000, text="PAUSED", font=(50,))

# start program
root.mainloop()
