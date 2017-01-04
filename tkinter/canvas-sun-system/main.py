#!/usr/bin/env python3

import tkinter as tk
import math

# --- functions ---

def calculate_position(data):
    #unpack data
    center_x, center_y, radius, distance, angle, angle_speed, x, y = data

    # calculate new position of object
    x = center_x - distance * math.sin(math.radians(-angle))
    y = center_y - distance * math.cos(math.radians(-angle))

    # save positon so other object can use it as its center of rotation
    data[6] = x
    data[7] = y

    # calcuate oval coordinates
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2

def create_object(data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    # create oval
    return c.create_oval(x1, y1, x2, y2)

def move_object(object_id, data):
    # calculate oval coordinates
    x1, y1, x2, y2 = calculate_position(data)

    # move oval
    c.coords(object_id, x1, y1, x2, y2)

def animate():
    # move earth - angle += angle_speed
    earth[4] += earth[5]
    move_object(e_id, earth)

    # moon uses earth position as center of rotation
    moon[0] = earth[6]
    moon[1] = earth[7]

    # move move - angle += angle_speed
    moon[4] += moon[5]
    move_object(m_id, moon)

    # animate again after 100ms
    root.after(100, animate)

# --- main ---

# canvas size
WIDTH  = 500
HEIGHT = 500

# center of solar system
center_x = WIDTH//2
center_y = HEIGHT//2

# objects data
# [center of rotation x and y, radius, distance from center, current angle, angle speed, current positon x and y]
sun   = [center_x, center_y, 30, 0, 0, 0, 0, 0]
earth = [center_x, center_y, 10, 100, 0, 1, 0, 0]
moon  = [0, 0, 5, 40, 0, 3, 0, 0]

# - init -
root = tk.Tk()
root.title("Solar System")

# - canvas -
c = tk.Canvas(root, width=WIDTH, heigh=HEIGHT)
c.pack()

# create sun and earth
s_id = create_object(sun)
e_id = create_object(earth)

# moon uses earth position as center of rotation
moon[0] = earth[6]
moon[1] = earth[7]

# create moon
m_id = create_object(moon)

# start animation
animate()

# - start program -
root.mainloop()
