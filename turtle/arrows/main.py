
# date: 2019.04.17
# https://stackoverflow.com/questions/55719351/how-to-tessellate-this-shape/55723100#55723100

import turtle

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
    if level > 0:
        move(length)
        figure(length, level-1)
    setup(length)

    if level > 0:
        move(length)
        figure(length, level-1)
    setup(length)

    if level > 0:
        move(length)
        figure(length, level-1)
    setup(length)

def move(length):
    t.penup()
    t.left(60)
    t.forward(length + length)
    t.right(60)
    t.pendown()

    
def example1(length):
    for _ in range(3):
        figure(length)
    
        t.penup()
        t.forward(length + length/3)
        t.right(120)
        t.backward(length/3)
        t.pendown()

def example2(length):
    for _ in range(3):
        figure(length)
    
        t.penup()
        t.left(60)
        t.forward(length + length)
        t.right(60)
        t.pendown()
    
def example3(length):
    figure(length, 2)
    
# --- main ---
t = turtle.Turtle()
t.left(30)
t.speed("fastest")
turtle.delay(0)
counter = 0 
t.begin_fill()

#example1(50)
#example2(50)
example3(50)
turtle.mainloop()
