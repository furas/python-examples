#!/usr/bin/env python

try:
    import Tkinter as tk # python 2.x
except:
    import tkinter as tk # python 3.x
    
from datetime import datetime

# --- constants ---

    # empty

# --- classes ---

    # empty
    
# --- function ---

def run():
    current_time = datetime.now()
    diff = current_time - start_time
    txt_var.set('%d.%02d' % (diff.seconds, diff.microseconds//10000))
    
    # run timer again after 100ms (0.1s) if not stoped
    if running:
        root.after(20, run)

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
    
def reset():
    global start_time

    start_time = datetime.now()
    if not running:
        txt_var.set('0.00')

# --- (global) vars ---

running = False
start_time = None

# --- main ---

root = tk.Tk()
root.title('Timer')

txt_var = tk.StringVar()
txt_var.set('0.00')
tk.Label(root, textvariable=txt_var).pack()

tk.Button(root, text='Start', command=start).pack(fill='x')
tk.Button(root, text='Stop',  command=stop ).pack(fill='x')
tk.Button(root, text='Reset', command=reset).pack(fill='x')

# start the engine :)    
root.mainloop()
