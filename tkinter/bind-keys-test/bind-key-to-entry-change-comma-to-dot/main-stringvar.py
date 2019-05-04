#!/usr/bin/env python3

import tkinter as tk

def callback(id_, mode, other):
    #print(id_, mode, other)
    var.set( var.get().replace(',', '.') )


root = tk.Tk()

var = tk.StringVar()
var.trace('w', callback)

e = tk.Entry(root, textvariable=var)
e.pack()

root.mainloop()
