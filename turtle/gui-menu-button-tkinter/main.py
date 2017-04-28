#!/usr/bin/env python3

# code: https://pastebin.com/Dz0kQWbq
# screen: http://imgur.com/SIISwwA

import turtle

def hello():
    print('Hello!')

def draw():
    turtle.forward(50)
    turtle.left(30)
    turtle.forward(50)
    turtle.left(30)

# access to tkinter - tk & root
# instead of standard
# import tkinter as tk
# root = tk.Tk()
tk = turtle.TK
screen = turtle.getscreen()
root = turtle.getscreen()._root

#root.set_geometry(500, 500, 0, 0)
#root.geometry('500x500')
#turtle.setup(width=500, height=500)

# create a toplevel menu
menubar = tk.Menu(root)
root.config(menu=menubar)

# create submenu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_command(label="Close", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

# create button
button = tk.Button(root, text="Draw", command=draw)
# add button to window
button.pack()

#turtle.done()
#turtle.mainloop()
root.mainloop()
