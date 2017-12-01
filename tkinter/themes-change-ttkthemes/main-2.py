#!/usr/bin/env python3

'''
ThemedStyle() can be created only once so I assign to variable 
and later assign variable to `root.style` many times

pip install ttkthemes
'''

import tkinter as tk
from tkinter import ttk
import ttkthemes

root = tk.Tk()

root.style = ttkthemes.ThemedStyle()
    
for i, name in enumerate(sorted(root.style.theme_names())):
    b = ttk.Button(root, text=name, command=lambda name=name:root.style.theme_use(name))
    b.pack(fill='x')

root.mainloop()
