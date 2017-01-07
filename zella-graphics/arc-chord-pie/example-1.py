from graphics import *

# --- constants ---

WIDTH = 300
HEIGHT = 300

# --- main ----

win = GraphWin("Patch", WIDTH, HEIGHT)

# area used by full circle
bbox = (5, 5, WIDTH-5, HEIGHT-5)

# create parts of circle - arc, chord, pieslice
win.create_arc(bbox, fill="red", outline='green', width=3, start=0,   extent=90, style='arc')
win.create_arc(bbox, fill="red", outline='green', width=3, start=95,  extent=90, style='chord')
win.create_arc(bbox, fill="red", outline='green', width=3, start=190, extent=90, style='pieslice')

#win.getKey()
win.getMouse()

win.close()
