#!/usr/bin/env python3

'''
Because after releasing keys `<Control-a>` selection is removed
so I use `after()` to execute selection after 50ms.
It selects all text (but it moves cursor to the beginning)
and moves cursor to the end.
'''

import tkinter as tk

def callback(event):
    print('e.get():', e.get())
    # or more universal
    print('event.widget.get():', event.widget.get())
    # select text after 50ms
    root.after(50, select_all, event.widget)

def select_all(widget):
    # select text
    widget.select_range(0, 'end')
    # move cursor to the end
    widget.icursor('end')

root = tk.Tk()

e = tk.Entry(root)
e.pack()
e.bind('<Control-a>', callback)

root.mainloop()
