#!/usr/bin/env python3

import tkinter as tk

# --- constants --- (UPPER_CASE names)

DISPLAY_WIDHT = 800
DISPLAY_HEIGHT = 600

CENTER_X = DISPLAY_WIDHT//2
CENTER_Y = DISPLAY_HEIGHT//2

# --- functions --- (lower_case names)

def move():

    # move if key pressed
    if key_up_arrow:
        canvas.move(a, 0, -5)
    elif key_down_arrow:
        canvas.move(a, 0, 5)

    # get current position
    x1, y1, x2, y2 = canvas.coords(a)

	# check collision with winow's border 
	# and stop on border or jump on other side 
	
	# jump on other side
    if y1 < -10: # check at top and jump when half of size (10) leave screen (object has height 20)
        canvas.move(a, a_speed_x, DISPLAY_HEIGHT) # jump from top to bottom
    if y2 > DISPLAY_HEIGHT+10: # check at bottom and jump when half of size (10) leave screen (object has height 20)
        canvas.move(a, a_speed_x, -DISPLAY_HEIGHT) # jump from bottom to top
 
     # stop aom border       
#    if y1 < 0: # check at top
#        canvas.move(a, a_speed_x, -y1) # stop at top
#    if y2 > DISPLAY_HEIGHT: # check at bottom
#        canvas.move(a, a_speed_x, DISPLAY_HEIGHT-y2) # stop it at bottom

    # move again after 25 ms (0.025s)
    root.after(25, move)

def up_arrow_press(event):
    global key_up_arrow
    key_up_arrow = True
    print('up_arrow press')

def up_arrow_release(event):
    global key_up_arrow
    key_up_arrow = False
    print('up_arrow release')

def down_arrow_press(event):
    global key_down_arrow
    key_down_arrow = True
    print('down_arrow press')

def down_arrow_release(event):
    global key_down_arrow
    key_down_arrow = False
    print('down_arrow release')


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

key_up_arrow = False
key_down_arrow = False
root.bind("<Up>", up_arrow_press) # Up Arrow
root.bind("<KeyRelease-Up>", up_arrow_release) # Up Arrow
root.bind("<Down>", down_arrow_press) # Down Arrow
root.bind("<KeyRelease-Down>", down_arrow_release) # Down Arrow

move()

# start program
root.mainloop()
