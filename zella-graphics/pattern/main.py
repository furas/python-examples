from graphics import *

def pattern():
    win = GraphWin("Rec", 100, 100)

    # horizontal lines
    for y in range(20, 100, 40):
        r = Rectangle(Point(0, y), Point(100, y+20))
        r.setFill("Green")
        r.setOutline("Green")
        r.draw(win)

    # vertical lines
    for x in range(0, 100, 40):
        r = Rectangle(Point(x, 0), Point(x+20, 100))
        r.setFill("Red")
        r.setOutline("Red")
        r.draw(win)

pattern()
