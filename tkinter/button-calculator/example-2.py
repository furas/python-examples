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

tk.Entry(root).pack(fill='x')

frame = tk.Frame(root)
frame.pack(fill='both', expand=True)
frame['bg'] = 'red'

for col in range(4):
    frame.columnconfigure(col, weight=1)
    frame.rowconfigure(col+1, weight=1)

for r, row in enumerate(buttons, 1):
    for c, text in enumerate(row):
        b = tk.Button(frame, text=text, command=lambda arg=text:callback(arg))
        b.grid(row=r, column=c, sticky='news')

root.mainloop()
