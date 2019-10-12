from turtle import *
from math import sin, cos, pi

shape("circle")
turtlesize(0.3)
speed(0)

#--- settings ---

# number of main lines
#n = int(input("give number of main lines: "))
n = 15

# length of main lines
#r = int(input("give length of main lines: "))
length = 200

# number of steps on every main line
steps = 5

#--- main lines ---

angle = 360/n
for i in range(n):
    forward(length)
    backward(length)
    right(angle)

#--- spiral ---

p = (length/n)/steps
rad = (pi*angle)/180

spiraldistance = 0
j = 0

while spiraldistance < length:
    spiraldistance += p
    x = cos(j) * spiraldistance
    y = sin(j) * spiraldistance
    goto(x, y)
    j += rad
    
#--- keep open ---

#mainloop()
exitonclick()
