#!/usr/bin/env python

import tkinter as tk

def second():
    global root
    
    # close first main window
    root.destroy()
    
    # create second main window 
    root = tk.Tk()
    tk.Button(root, text='Close', command=root.destroy).pack()
    root.mainloop()
    
# create first main window     
root = tk.Tk()
tk.Button(root, text='Submit', command=second).pack()
root.mainloop()
