#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_change():
    print('Check it:', var.get())

# --- main ---

root = tk.Tk()

#var = tk.BooleanVar(value=False)
var = tk.BooleanVar()

#tk.Checkbutton(root, text='OK', variable=var, command=on_change).pack()
cb = tk.Checkbutton(root, text='Check it', variable=var, command=on_change)
cb.pack()

root.mainloop()
