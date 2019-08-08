#!/usr/bin/env python

import tkinter as tk

# --- functions ---

def open_second_window():
    global root
    
    # close first main window
    root.destroy()
    
    # open second main window 
    root = tk.Tk()
    tk.Button(root, text='Close', command=root.destroy).pack()
    root.mainloop()

# --- main ---
    
# open first main window     
root = tk.Tk()
tk.Button(root, text='Submit', command=open_second_window).pack()
root.mainloop()
