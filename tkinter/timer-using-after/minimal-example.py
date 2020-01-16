#!/usr/bin/env python3

# date: 2020.01.14

import tkinter as tk
import time

# --- functions ---

def update_time():
    label['text'] = time.strftime('%Y.%m.%d  %H:%M:%S')

    # run update_time again after 1000ms (1s)
    root.after(1000, update_time)

# --- main ---

root = tk.Tk()

label = tk.Label(root)
label.pack()

# run update_time first time
update_time()

root.mainloop()
