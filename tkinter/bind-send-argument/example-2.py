#!/usr/bin/env python3

'''Assign extra parameter to instance'''

import tkinter as tk

# --- functions ---

def callback(event):
    print(' Text:', event.widget['text'])
    print('Extra:', event.widget.extra) # extra parameter

# --- main ---

root = tk.Tk()

w = tk.Label(root, text="Click here")
w.pack()
w.bind("<Button-1>", callback)
w.extra = "Hello World" # extra parameter

root.mainloop()
