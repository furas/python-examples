#!/usr/bin/env python3

# date: 2019.09.29
# https://stackoverflow.com/questions/58156975/how-to-use-letter-keys-in-turtle

import turtle

def forward():
    turtle.setheading(90)
    turtle.forward(100)

def backward():
    turtle.setheading(270)
    turtle.forward(100)

def left():
    turtle.setheading(180)
    turtle.forward(100)

def right():
    turtle.setheading(0)
    turtle.forward(100)

turtle.onkey(forward, 'w')
turtle.onkey(backward, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')

turtle.listen()

#turtle.mainloop()
turtle.exitonclick()
