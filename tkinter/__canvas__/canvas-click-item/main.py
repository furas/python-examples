#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_click_canvas(event):
    print(' event:', event)
    print('widget:', event.widget)
    print('serial:', event.serial)
    x, y = event.x, event.y
    ids = canvas.find_overlapping(x, y, x+1, y+1)
    if ids:
        print('ids:', ids)
        canvas.delete(ids[-1])


def on_click_tag(tags=None):
    print('tags:', tags)
    canvas.delete(tags)

# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

canvas.create_line(0, 0, 200, 100)
canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

rect = canvas.create_rectangle(50, 25, 150, 75, fill="blue")
#canvas.tag_bind(rect, '<Button-1>', lambda event:canvas.delete(rect))
canvas.tag_bind(rect, '<Button-1>', lambda event, tag=rect: on_click_tag(tag))
#canvas.bind('<Button-1>', on_click_canvas)

root.mainloop()
