#!/usr/bin/env python

# https://studio.code.org/c/35859693/edit

import turtle

# --- functions ---

def draw_1(length, level):
    if level < 1:
        turtle.fd(length)
    else:
        length = length/3
        
        draw_1(length, level-1)
        turtle.left(90)
        draw_1(length, level-1)
        turtle.right(90)
        draw_1(length, level-1)
        turtle.right(90)
        draw_1(length, level-1)
        turtle.left(90)
        draw_1(length, level-1)

def draw_2(length, level):
    if level < 1:
        turtle.fd(length)
    else:
        length = length/3
        
        draw_2(length, level-1)
        turtle.left(60)
        draw_2(length, level-1)
        turtle.right(180-60)
        draw_2(length, level-1)
        turtle.left(60)
        draw_2(length, level-1)

def turn_left(width, step, draw):
    for _ in range(4):
        draw(width, step)
        turtle.left(90)

def turn_right(width, step, draw):
    for _ in range(4):
        draw(width, step)
        turtle.right(90)

# --- main ---

# clear everything
turtle.reset()

# the fastest turtle
turtle.speed(0)



turn_right(300, 3, draw_2)
turtle.left(90)
turn_right(300, 3, draw_2)



# hide turtle
turtle.hideturtle()

# keep open window
turtle.exitonclick()
