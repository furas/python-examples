#!/usr/bin/env python3

'''
Before I couldn't find correct combination with `Release`
but it has to be `<Control-KeyRelease-a>`
and now it doesn't need `after()`
'''

import tkinter as tk

def callback(event):

    print('e.get():', e.get())
    # or more universal
    print('event.widget.get():', event.widget.get())

    # select text
    event.widget.select_range(0, 'end')
    # move cursor to the end
    event.widget.icursor('end')

root = tk.Tk()

e = tk.Entry(root)
e.pack()
e.bind('<Control-KeyRelease-a>', callback)

root.mainloop()
