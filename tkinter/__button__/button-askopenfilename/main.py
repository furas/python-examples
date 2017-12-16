#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog

# --- functions ---

def on_click():
    filename = filedialog.askopenfilename()
    if filename:
        print("Filename:", filename)
    else:
        print("Filename: not selected")

# --- main ---

root = tk.Tk()

tk.Button(root, text='Click Me', command=on_click).pack()

root.mainloop()
