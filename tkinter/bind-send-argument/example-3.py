#!/usr/bin/env python3

'''Use extra parameter in bind'''

import tkinter as tk

# --- functions ---

def callback(event, extra):
    print(' Text:', event.widget['text'])
    print('Extra:', extra)

# --- main ---

root = tk.Tk()

w = tk.Label(root, text="Click here")
w.pack()
w.bind("<Button-1>", lambda event:callback(event, "Hello World"))

root.mainloop()
