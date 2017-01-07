from graphics import *

# --- constants ---

WIDTH = 300
HEIGHT = 300

# --- functions ---

def moves():

    # move figure 1
    s = win.itemcget(fig1, 'start')
    win.itemconfig(fig1, start=float(s)+5)

    # move figure 2
    s = win.itemcget(fig2, 'start')
    win.itemconfig(fig2, start=float(s)+5)

    # move figure 3
    s = win.itemcget(fig3, 'start')
    win.itemconfig(fig3, start=float(s)+5)

    # run again after 100ms (0.1s)
    win.after(100, moves)

# --- main ----

win = GraphWin("Patch", WIDTH, HEIGHT)

bbox = (5, 5, WIDTH-5, HEIGHT-5)

fig1 = win.create_arc(bbox, fill="red", outline='green', width=3, start=0,   extent=90, style='arc')
fig2 = win.create_arc(bbox, fill="red", outline='green', width=3, start=95,  extent=90, style='chord')
fig3 = win.create_arc(bbox, fill="red", outline='green', width=3, start=190, extent=90, style='pieslice')

# run first time - to start animation
moves()

#win.getKey()
win.getMouse()

win.close()
