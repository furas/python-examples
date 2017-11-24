#!/usr/bin/env python3

from graphics import *

STEP = 10

win = GraphWin('Example', 300, 300)

for x1 in range(0, 301, STEP):
    x2 = x1 + STEP
    Line(Point(x1, 0), Point(300, x2)).draw(win)
    Line(Point(300-x1, 0), Point(0, x2)).draw(win)
    Line(Point(0, x2), Point(x1, 300)).draw(win)
    Line(Point(300, x2), Point(300-x1, 300)).draw(win)
    
win.getMouse()
win.close()
