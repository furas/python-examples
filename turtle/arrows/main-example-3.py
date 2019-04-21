
# date: 2019.04.17
# https://stackoverflow.com/questions/55719351/how-to-tessellate-this-shape/55723100#55723100

import turtle
import time

# --- functions ---

def setup(length):
    t.forward(length)
    t.right(120)
    t.forward(length / 3)
    t.left(60)
    t.forward(length / 3)
    t.left(120)
    t.forward(length)
    t.left(60)
    t.forward(length)
    t.left(120)
    t.forward(length / 3)
    t.left(60)
    t.forward(length / 3)
    t.right(120)
    t.forward(length)
    t.right(60)

def figure(length, level=0):
	for _ in range(3):
		time.sleep(1)
		if level > 0:
		    move1(length)
		    figure(length, level-1)
		    move2(length)

		setup(length)

def move1(length):
    t.penup()
    t.forward(length + length/3)
    t.right(120)
    t.backward(length/3)
    t.pendown()

def move2(length):
    t.penup()
    t.backward(-length/3)
    t.right(-120)
    t.forward(-(length + length/3))
    t.pendown()


# --- main ---

t = turtle.Turtle()
t.speed(0)
turtle.delay(0)

t.left(30)

figure(50, 2)

turtle.mainloop()
