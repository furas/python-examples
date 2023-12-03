#!/usr/bin/env python3

"""
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2017.01.13
# [How to Close Python Turtle Properly - Stack Overflow](https://stackoverflow.com/questions/41644324/how-to-close-python-turtle-properly/41644914#41644914)
"""

import turtle as t

t.goto(0,50)
t.exitonclick()

t.TurtleScreen._RUNNING = True   # solution for `turtle.Terminator` error

t.goto(50,150)
t.exitonclick()

t.TurtleScreen._RUNNING = True   # solution for `turtle.Terminator` error

# ... other code ...
