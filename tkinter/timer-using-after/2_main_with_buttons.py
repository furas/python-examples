#!/usr/bin/env python

try:
    import Tkinter as tk # python 2.x
except:
    import tkinter as tk # python 3.x
    
from datetime import datetime

# --- function ---

def start():
    global running
    global start_time

    if not running:
        running = True
        start_time = datetime.now()
        
        root.after(10, run)

def stop():
    global running

    running = False
    
def run():
    current_time = datetime.now()
    diff = current_time - start_time
    txt.set('%d.%02d' % (diff.seconds, diff.microseconds//10000))
    
    # run timer after 100ms (0.1s)
    if running:
        root.after(20, run)

def reset():
    global start_time

    if running:
        start_time = datetime.now()

# --- vars ---

running = False
start_time = None

# --- main ---

root = tk.Tk()
root.title('Timer')

txt = tk.StringVar()
tk.Label(root, textvariable=txt).pack()

tk.Button(root, text='Start', command=start).pack(fill='x')
tk.Button(root, text='Stop', command=stop).pack(fill='x')
tk.Button(root, text='Reset', command=reset).pack(fill='x')
    
root.mainloop()
