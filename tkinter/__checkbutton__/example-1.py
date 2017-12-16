#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_change():
    # get Checkbutton
    print('Check it:', var.get())

# --- main ---

root = tk.Tk()

# -----

#var = tk.BooleanVar(value=False) # set value at start
var = tk.BooleanVar() # default value False

#tk.Checkbutton(root, text='Check it', variable=var, command=on_change).pack()
cb = tk.Checkbutton(root, text='Check it', variable=var, command=on_change)
cb.pack()

var.set(True) # changes Checkbutton

# -----

root.mainloop()
