#!/usr/bin/env python3

'''
ThemedStyle() can be created only once so I assign to variable 
and later assign variable to `root.style` many times

pip install ttkthemes
'''

import tkinter as tk
from tkinter import ttk
import ttkthemes

def style_1():
    print('winxpblue')
    root.style = s
    root.style.theme_use('winxpblue')

def style_2():
    print('black')
    root.style = t
    root.style.theme_use('black')
    
root = tk.Tk()

s = ttk.Style()
t = ttkthemes.ThemedStyle()

#print(s.theme_names())
#print(t.theme_names())

ttk.Button(root, text="1", command=style_1).pack()
ttk.Button(root, text="2", command=style_2).pack()

root.mainloop()
