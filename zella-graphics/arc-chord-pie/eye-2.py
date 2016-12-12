from graphics import *

# --- constants ---

WIDTH = 300
HEIGHT = 300

# --- main ----

win = GraphWin("EXAMPLE", WIDTH, HEIGHT)

# ---

RADIUS = 50

bbox = (0, -RADIUS/2, RADIUS*2, RADIUS*2-RADIUS/2)
win.create_arc(bbox, fill="blue", outline="blue", extent=120, style='chord', start=30+180)

bbox = (0, RADIUS/2, RADIUS*2, RADIUS*2+RADIUS/2)
win.create_arc(bbox, fill="blue", outline="blue", extent=120, style='chord', start=30)

#bbox = (0, -75, RADIUS*2, RADIUS*2-75)
#win.create_arc(bbox, fill="blue", outline="blue", extent=120, style='chord', start=30+180)

#bbox = (0, 75, 300, 300+75)
#win.create_arc(bbox,  fill="blue", outline="blue", extent=120, style='chord', start=30)

# ---

#win.create_oval((100, 100, 200, 200), fill="white", outline="white")
#win.create_oval((130, 130, 170, 170), fill="black", outline="black")

# ---
#win.getKey()
win.getMouse()

win.close()
