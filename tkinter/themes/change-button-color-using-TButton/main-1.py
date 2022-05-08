#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk

def red_buttons():
    s.configure('TButton', background='red')
    root.after(200, green_buttons)
    
def green_buttons():
    s.configure('TButton', background='green')
    root.after(200, red_buttons)

root = tk.Tk()

s = ttk.Style()
s.configure('TButton', background='pink')#, foreground='red')

ttk.Button(root, text="1").pack()
ttk.Button(root, text="2").pack()

root.after(2000, red_buttons)

root.mainloop()
