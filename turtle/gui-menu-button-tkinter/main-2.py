#!/usr/bin/env python3

# code: https://pastebin.com/Dz0kQWbq
# screen: http://imgur.com/SIISwwA

import turtle

def hello():
    print('Hello!')

# access to tkinter - tk & root
# instead of standard
# import tkinter as tk
# root = tk.Tk()
tk = turtle.TK
screen = turtle.getscreen()
root = screen._root
canvas = screen._canvas

#root.set_geometry(500, 500, 0, 0)
root.geometry('500x500')
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

frame = tk.Frame(root)
#frame.pack(before=canvas)
#frame.pack(side='right')
frame.pack()#fill='y', expand=True)
# create button
button = tk.Button(frame, text="forward 50", command=lambda:turtle.forward(50))
button.grid(row=0, column=0, sticky='we')

button = tk.Button(frame, text="forward 10", command=lambda:turtle.forward(10))
button.grid(row=0, column=1, sticky='we')

button = tk.Button(frame, text="backward 10", command=lambda:turtle.backward(10))
button.grid(row=0, column=2, sticky='we')

button = tk.Button(frame, text="backward 50", command=lambda:turtle.backward(50))
button.grid(row=0, column=3, sticky='we')


button = tk.Button(frame, text="left 90", command=lambda:turtle.left(90))
button.grid(row=1, column=0, sticky='we')

button = tk.Button(frame, text="left 30", command=lambda:turtle.left(30))
button.grid(row=1, column=1, sticky='we')

button = tk.Button(frame, text="right 30", command=lambda:turtle.right(30))
button.grid(row=1, column=2, sticky='we')

button = tk.Button(frame, text="right 90", command=lambda:turtle.right(90))
button.grid(row=1, column=3, sticky='we')

#turtle.done()
#turtle.mainloop()
root.mainloop()
