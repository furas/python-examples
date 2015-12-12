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

size = 10
steps = 36
move = 10

for _ in range(2):
    
    for _ in range(steps//4):
        draw_rectangle(size)
        turtle.right(360/steps)
        turtle.up()
        turtle.forward(move)
        turtle.down()

    for _ in range(steps//4):
        draw_rectangle(size)
        turtle.left(360/steps)
        turtle.up()
        turtle.forward(move)
        turtle.down()

    for _ in range(steps//4):
        draw_rectangle(size)
        turtle.left(360/steps)
        turtle.up()
        turtle.forward(move)
        turtle.down()

    for _ in range(steps//4):
        draw_rectangle(size)
        turtle.right(360/steps)
        turtle.up()
        turtle.forward(move)
        turtle.down()


# keep open window
turtle.exitonclick()
