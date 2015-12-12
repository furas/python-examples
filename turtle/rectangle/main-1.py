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


draw_rectangle(100)
draw_rectangle(200)
draw_rectangle(300)


# keep open window
turtle.exitonclick()
