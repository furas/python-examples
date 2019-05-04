#!/usr/bin/env python3

import tkinter as tk

def callback(event):
    print('event.widget.get():', event.widget.get())
    text = event.widget.get()     # get all text
    text = text.replace(',', '.') # replace comma
    event.widget.delete(0, 'end') # remove all text from Entry
    event.widget.insert(0, text)  # put new text in Entry


root = tk.Tk()

e = tk.Entry(root)
e.pack()
e.bind('<KeyRelease-comma>', callback) # execute after it put comma in Entry

root.mainloop()
