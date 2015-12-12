#!/usr/bin/env python3

from turtle import *
 
def f(length, depth):
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
 
def flake(length, depth, count):
    begin_fill()

    f(length, depth)
    if count > 0:
        flake(length, depth, count-1)
        left(120)
    left(120)

    f(length, depth)
    if count > 0:
        flake(length, depth, count-1)
        left(120)
    left(120)

    f(length, depth)
    if count > 0:
        flake(length, depth, count-1)
        left(120)
    left(120)

    end_fill()
    
reset()              
speed(0)
flake(100, 2, 2)
#flake(100, 2)
#flake(100, 2)
