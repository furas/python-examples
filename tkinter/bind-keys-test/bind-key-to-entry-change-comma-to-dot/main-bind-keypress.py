#!/usr/bin/env python3

import tkinter as tk

def callback(event):
    #print('event.widget.get():', event.widget.get())
    event.widget.insert('end', '.')  # put new text in Entry
    return 'break' # stop event so it will not put comma in Entry

root = tk.Tk()

e = tk.Entry(root)
e.pack()
e.bind('<Key-comma>', callback) # execute callback before it puts comma in Entry

root.mainloop()
