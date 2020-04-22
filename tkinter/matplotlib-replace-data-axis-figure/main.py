#!/usr/bin/env python3

# date: 2020.03.30

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# --- functions ---

def clear_data():
    datax = []
    datay = []

    plot[0].set_data(datax, datay)
    
    canvas.draw()

def replace_data():
    datax = range(10)
    datay = [x/10 for x in random.sample(range(10), 10)]
    
    plot[0].set_data(datax, datay)
    
    canvas.draw()

def clear_axis():
    global plot 

    axis.clear()
    #axis.cla()
    
    canvas.draw()

def replace_axis():
    global plot 

    axis.clear()
    #axis.cla()
    
    datax = range(10)
    datay = [x/10 for x in random.sample(range(10), 10)]

    plot = axis.plot(datax, datay)

    canvas.draw()

def clear_figure():
    fig.clear()
    #fig.clf()

    canvas.draw()

def replace_figure():
    global fig
    global axis
    global plot 

    fig.clear()
    #fig.clf()

    # create figure, axis, canvas
    fig = Figure(figsize=(5, 5))
    axis = fig.add_subplot(111)
    canvas.figure = fig
    
    datax = range(10)
    datay = [x/10 for x in random.sample(range(10), 10)]

    plot = axis.plot(datax, datay)

    canvas.draw()
    
# --- main ---

root = tk.Tk()

datax = range(10)
datay = [x/10 for x in random.sample(range(10), 10)]

# create figure, axis, canvas
fig = Figure(figsize=(5, 5))
axis = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

# plot data
plot = axis.plot(datax, datay)

# redraw (if needed)
#canvas.draw()

# buttons

frame = tk.Frame(root)
frame.pack()

b = tk.Button(frame, text='Clear data', command=clear_data)
b.grid(row=0, column=0, sticky='we')

b = tk.Button(frame, text='Replace data', command=replace_data)
b.grid(row=0, column=1, sticky='we')

b = tk.Button(frame, text='Clear axis', command=clear_axis)
b.grid(row=1, column=0, sticky='we')

b = tk.Button(frame, text='Replace axis', command=replace_axis)
b.grid(row=1, column=1, sticky='we')

b = tk.Button(frame, text='Clear figure', command=clear_figure)
b.grid(row=2, column=0, sticky='we')

b = tk.Button(frame, text='Replace figure', command=replace_figure)
b.grid(row=2, column=1, sticky='we')
              
root.mainloop()
