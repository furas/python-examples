#!/usr/bin/env python3

import turtle

# --- functions ---

def flower(size):
    for _ in range(36):
        turtle.forward(size)
        turtle.left(110)

# --- main ---

# clear everything
turtle.reset()

# the fastest turtle
turtle.speed(0) 


flower(100)

turtle.hideturtle()


# keep open window
turtle.exitonclick()
