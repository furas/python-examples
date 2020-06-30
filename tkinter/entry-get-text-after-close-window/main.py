#!/usr/bin/env python3

# date: 2020.06.27

import tkinter as tk
        
# --- functions ---

def on_click():
    global result

    result = entry.get()

    print('[before] result   :', result)   # OK - before destroying window
    print('[before] StringVar:', msg.get())   # OK - before destroying window
    print('[before] Entry    :', entry.get()) # OK - before destroying window

    root.destroy()

# --- main ---

result = "" # variable for text from `Entry`

root = tk.Tk()

msg = tk.StringVar(root)
entry = tk.Entry(root, textvariable=msg)
entry.pack()

button = tk.Button(root, text='Close', command=on_click)
button.pack()

root.mainloop()

# --- after closing window ---

print('[after] result   :', result)      # OK    - after destroying window
print('[after] StringVar:', msg.get())   # OK    - after destroying window
print('[after] Entry    :', entry.get()) # ERROR - after destroying window
