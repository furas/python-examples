import turtle
import math

def draw_rectangle(width, height, color='red'):
    turtle.pd()
    turtle.color(color)

    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def draw_circle(radius, color='red'):
    turtle.pd()
    turtle.color(color)
    turtle.circle(radius)


def draw_pattern_rectangle(x, y, width, height, count, radius, color='red'):
    rotation = 360 / count

    turtle.goto(x, y)
    
    for _ in range(count):
        # move from center to circle
        turtle.pu()
        #turtle.color('black')
        turtle.forward(radius)
        turtle.right(90+rotation/2)
        
        draw_rectangle(width, height, color)

        # move from circle to center
        turtle.pu()
        #turtle.color('black')
        turtle.left(90+rotation/2)
        turtle.backward(radius)

        # rotate in circle
        turtle.right(rotation)

def draw_pattern_circle(x, y, r, count, radius, color='red'):
    rotation = 360 / count

    turtle.goto(x, y)

    for _ in range(count):
        # move from center to circle
        #turtle.pu()
        turtle.color('black')
        turtle.forward(radius)
        turtle.right(90)

        draw_circle(r, color)

        # move from circle to center
        #turtle.pu()
        turtle.color('black')
        turtle.left(90)
        turtle.backward(radius)

        # rotate in circle
        turtle.right(rotation)
        
turtle.speed(0)
        
#draw_pattern_rectangle(0, 0, 100, 100, 15, 50)
#draw_pattern_circle(0, 0, 20, 15, 20, 'blue')
#draw_pattern_circle(0, 0, 20, 15, 150, 'green')

for radius in range(10, 151, 40):
    draw_pattern_circle(0, 0, 20, 5, radius, 'blue')
#    draw_pattern_circle(0, 0, 20, 15, radius+10, 'green')

steps = 40
for radius in range(steps):
    draw_circle(10)
    turtle.forward(10)
    turtle.left(360/steps)

turtle.exitonclick()


