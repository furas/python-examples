#!/usr/bin/env python3 

# date: 2019.11.30
# https://stackoverflow.com/questions/59111688/solar-system-in-python

import turtle
import math

mars = turtle.Turtle()
earth = turtle.Turtle()
spacecraft = turtle.Turtle()

def way_to_orbit(x,y, object, colors):
    object.dot(50, "yellow")
    object.color("white")
    object.fillcolor(colors)
    object.shape("circle")
    object.penup()
    object.setposition(x, y)
    object.pendown()


def move(object1, object2, object3):

    loop = True
    object2_xvel = 0
    object2_yvel = 1
    object1_xvel = 0
    object1_yvel = 1
    object3_xvel = 0
    object3_yvel = 1
    a = 0
    while loop:

        rad = math.radians(object1.towards(0, 0))
        distance = 1000 / (object1.xcor()**2 + object1.ycor()**2)
        object1_xvel += math.cos(rad) * distance
        object1_yvel += math.sin(rad) * distance
        object1.setposition(object1.xcor() + object1_xvel, object1.ycor() + object1_yvel)

        rad = math.radians(object2.towards(0, 0))
        distance = 1000 / (object2.xcor()**2 + object2.ycor()**2)
        object2_xvel += math.cos(rad) * distance
        object2_yvel += math.sin(rad) * distance
        object2.setposition(object2.xcor() + object2_xvel, object2.ycor() + object2_yvel)

        object3.setposition(object3.xcor() + object2_xvel, object3.ycor() + object2_yvel)

        rad = math.radians(object3.towards(object2.xcor(), object2.ycor()))
        distance = 1000 / ( (object3.xcor()-object2.xcor())**2 + (object3.ycor()-object2.ycor())**2 )
        object3_xvel = math.cos(rad) * distance
        object3_yvel = math.sin(rad) * distance
        object3.setposition(object3.xcor() + object3_xvel, object3.ycor() + object3_yvel)

way_to_orbit(620, 0, mars, "red")
way_to_orbit(375, 0, earth, "blue")
way_to_orbit(396, 0, spacecraft, "green")

ellipse(mars, earth, spacecraft)


turtle.done()
