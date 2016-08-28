#!/usr/bin/env python

try:
    import Tkinter as tk # python 2.x
except:
    import tkinter as tk # python 3.x
    
from datetime import datetime

# --- function ---

def timer():
    txt.set(datetime.now().strftime('%Y.%m.%d  %H:%M:%S'))
    # run timer again after 1000ms (1s)
    root.after(1000, timer)

# --- main ---

root = tk.Tk()
root.title('Time')

txt = tk.StringVar()
tk.Label(root, textvariable=txt).pack()

# run timer first time
timer()
# or timer first time after 1000ms (1s)
# root.after(1000, timer)

root.mainloop()
