#!/usr/bin/env python3

import turtle as t
import random

def move():
    if running:
        t.forward(15)
        angle = random.randint(-9, 9) * 10 
        t.left(angle)
        t.ontimer(move, 25) # 25ms

running = True
move()
t.exitonclick()
running = False
