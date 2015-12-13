#!/usr/bin/env python

try:
    import Tkinter as tk
except: 
    import tkinter as tk

def open_subwindow():
    subwindow = tk.Toplevel()
    subwindow.geometry("300x300")
    btn = tk.Button(subwindow, text="Close subwindow", command=subwindow.destroy)
    btn.pack()
    
root = tk.Tk()

btn = tk.Button(root, text="Open subwindow", command=open_subwindow)
btn.pack()

root.mainloop()
