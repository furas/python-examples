#!/usr/bin/env python3

# date: 2020.01.21
# ???

import tkinter as tk

# --- functions ---

def solve():

    x = float(entry_x.get()) 
    y = float(entry_y.get())
    z = eval(equation.get())
    z_var.set("{0:.3f}".format(z))

# --- main ---

root = tk.Tk()

z_var = tk.StringVar()

tk.Label(root, text="Equation").grid(row=0, column=0)
equation = tk.Entry(root)
equation.grid(row=0, column=1)

tk.Label(root, text="x =").grid(row=1, column=0, sticky='e')
entry_x = tk.Entry(root)
entry_x.grid(row=1, column=1)

tk.Label(root, text="y =").grid(row=2, column=0, sticky='e')
entry_y = tk.Entry(root)
entry_y.grid(row=2, column=1)

tk.Label(root, text="z =").grid(row=3, column=0, sticky='e')
tk.Label(root, textvariable=z_var, anchor='w').grid(row=3, column=1, sticky='we')

button = tk.Button(root, text="Solve", command=solve)
button.grid(row=4, column=0, columnspan=2, sticky='we')

entry_x.insert('end', '3')
entry_y.insert('end', '4')
equation.insert('end', '(x**2 + y**2)**0.5')
solve()

root.mainloop()
