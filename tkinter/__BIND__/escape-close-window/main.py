#!/usr/bin/env python3 

# date: 2020.01.02
# ???


import tkinter as tk

# --- functions ---

def stop(event):
    root.destroy()
   
# --- main ---

root = tk.Tk()

root.bind('<Escape>', stop)
root.focus()

root.mainloop()
