#!/usr/bin/env python3

from tkinter import *

def test(event=None, ids=None):
    if event:
        print(dir(event))
        print(event)
        print(event.widget)
        print(event.serial)
        x, y = event.x, event.y
        ids = w.find_overlapping(x, y, x+1, y+1)
        if ids:
            w.delete(ids[-1])
    if ids:
        w.delete(ids)

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

r = w.create_rectangle(50, 25, 150, 75, fill="blue")
print(r)
#w.bind('<Button-1>', test)
w.tag_bind(r, '<Button-1>', lambda event, i=r:test(ids=i))

mainloop()
