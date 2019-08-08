#!/usr/bin/env python

import tkinter as tk

# --- functions ---

def open_subwindow():
    subwindow = tk.Toplevel()
    subwindow.geometry("300x300")

    btn = tk.Button(subwindow, text="Close subwindow", command=subwindow.destroy)
    btn.pack()
    
# --- main ---    

root = tk.Tk()

btn = tk.Button(root, text="Open subwindow", command=open_subwindow)
btn.pack()

root.mainloop()
