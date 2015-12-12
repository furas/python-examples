#!/usr/bin/env python

# https://studio.code.org/c/35859693/edit

import turtle

# --- functions ---

def gear(count, width, height):

    angle = 90-(180/count)

    for _ in range(count):
        turtle.forward(width)
        turtle.left(angle)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.left(angle)

# --- main ---

# clear everything
turtle.reset()

# the fastest turtle
turtle.speed(0)



gear(36, 10, 10)



# hide turtle
turtle.hideturtle()

# keep open window
turtle.exitonclick()
