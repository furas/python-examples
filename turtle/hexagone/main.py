import turtle
from math import pi, sin, cos

def hexagone(point, longueur,c):
   l = longueur

   x, y = point

   turtle.up()
   turtle.goto(point)
   turtle.color(c[0]) #black
   turtle.down()
   turtle.begin_fill() 
   turtle.goto(l * cos(4 / 3 * pi )+x, l * sin(4 / 3 * pi)+y)
   turtle.goto(l * cos(5 / 3 * pi)+x, l * sin(5 / 3 * pi)+y)
   turtle.goto(l * cos(0)+x, l * sin(0)+y) 
   turtle.goto(point) 
   turtle.end_fill()

   turtle.color(c[1])  #blue
   turtle.begin_fill()
   turtle.goto(l * cos(0)+x, l * sin(0)+y) 
   turtle.goto(l * cos(pi / 3)+x, l * sin(pi / 3)+y)
   turtle.goto(l * cos(pi * 2 / 3)+x, l * sin(pi * 2 / 3)+y)
   turtle.goto(point)  
   turtle.end_fill()

   turtle.color(c[2]) #red
   turtle.begin_fill()
   turtle.goto(l * cos(pi * 2 / 3)+x, l * sin(pi * 2 / 3)+y)
   turtle.goto(-l+x, 0+y)
   turtle.goto(l * cos(4 / 3 * pi)+x, l * sin(4 / 3 * pi)+y)
   turtle.goto(point)
   turtle.end_fill()
   turtle.up()

   return True

hexagone((0,0), 50, ("black",("blue"),("red")))
hexagone((100,0), 50, ("black",("blue"),("red")))
hexagone((0,100), 50, ("black",("blue"),("red")))
hexagone((100,100), 50, ("black",("blue"),("red")))
turtle.done()

