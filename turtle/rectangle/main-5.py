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

steps = 36
move = 10

for _ in range(steps):
    draw_rectangle(100)
    turtle.right(360/steps)
    turtle.forward(move)


# keep open window
turtle.exitonclick()
