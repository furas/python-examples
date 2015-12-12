#!/usr/bin/env python3

import turtle

# --- functions ---

def draw_rectangle(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

# --- main ---

# clear everything
turtle.reset()

# the fastest turtle
turtle.speed(0) 


for size in range(10, 300, 10):
    draw_rectangle(size)
    turtle.right(15)


# keep open window
turtle.exitonclick()
