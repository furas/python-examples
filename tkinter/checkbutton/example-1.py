#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_button():
    print('OK:', var.get())

# --- main ---

root = tk.Tk()

#var = tk.BooleanVar(value=False)
var = tk.BooleanVar()

#tk.Checkbutton(root, text='OK', variable=var, command=on_button).pack()
cb = tk.Checkbutton(root, text='OK', variable=var, command=on_button)
cb.pack()

root.mainloop()
