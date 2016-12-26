#!/usr/bin/env python3

'''Get starndard parameters'''

import tkinter as tk

# --- functions ---

def callback(event):
    print('Text:', event.widget['text'])

# --- main ---

root = tk.Tk()

w = tk.Label(root, text="Click here")
w.pack()
w.bind("<Button-1>", callback)

root.mainloop()
