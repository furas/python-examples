#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def callback(x):
    print(x)

# --- main ---

buttons = [
  ("1", "2", "3", "+"),
  ("4", "5", "6", "-"),
  ("7", "8", "9", "*"),
  (".", "0", "=", "/"),
]

root = tk.Tk()
root.title("Calculator")
root['bg'] = 'red'

tk.Entry(root).grid(row=0, columnspan=4, sticky='we')

for r, row in enumerate(buttons, 1):
    for c, text in enumerate(row):
        b = tk.Button(root, text=text, command=lambda arg=text:callback(arg))
        b.grid(row=r, column=c, sticky='news')

for col in range(4):
    root.columnconfigure(col, weight=1)
    root.rowconfigure(col+1, weight=1)

root.mainloop()
