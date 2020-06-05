#!/usr/bin/env python3

# date: 2020.05.29
# It use after to animate point and you still can click window to close program

from graphics import * # PEP8: `import *` is not preferred 
import random

# --- functions ---

def move():
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    pt.move(dx, dy)
    # move again after 100ms (0.1s)
    win.after(100, move)

# --- main ---

win = GraphWin("My Window",500,500)
win.setBackground(color_rgb(0,0,0))

pt = Point(250, 250)
pt.setOutline(color_rgb(255,255,0))
pt.draw(win)

# move first time after 100ms (0.1s)
win.after(100, move)

#win.mainloop()
win.getMouse()

win.close()
