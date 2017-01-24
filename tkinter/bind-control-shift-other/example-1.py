#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def key_f(event):
    print('key: f')

def key_control_f(event):
    print('key: Control + f')

def key_shift_f(event):
    print('key: Shift + f')

def key_control_shift_f(event):
    print('key: Control+Shift + f')

# --- main ---

root = tk.Tk()

#root.bind("<f>", key_f)
#root.bind("<F>", key_shift_f)
root.bind("f", key_f)
root.bind("F", key_shift_f)
root.bind("<Control-f>", key_control_f)
root.bind("<Control-F>", key_control_shift_f)

root.mainloop()
