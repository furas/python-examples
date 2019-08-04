#!/usr/bin/env python3

#
# http://matplotlib.org/examples/user_interfaces/embedding_in_tk.html
#
# update: 2019.08.03
# 
# NavigationToolbar2TkAgg is deprecate since 2.2 and doesn't work in 3.1.1
# so now it uses NavigationToolbar2Tk
# 
# FigureCanvasTk doesn't display plot but it still shows coordinates in navigation bar
# so it still uses FigureCanvasTkAgg
#

import matplotlib 
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    #FigureCanvasTk, # doesn't display plot but it still shows coordinates in navigation bar
    #NavigationToolbar2TkAgg, deprcated in 2.2 and doesn't work in 3.1.1
    NavigationToolbar2Tk
)
from matplotlib.pyplot import Figure

import tkinter as tk


# --- random data ---

import random
import math

y1 = [random.randint(-100, 100) for x in range(60)]
y2 = [math.sin(math.radians(x*6)) for x in range(60)]

# --- GUI ---

root = tk.Tk()

# top frame for canvas and toolbar - which need `pack()` layout manager
top_frame = tk.Frame(root)
top_frame.pack()

# bottom frame for other widgets - which may use other layout manager 
bottom_frame = tk.Frame(root)
bottom_frame.pack()

# --- canvas and toolbar in top ---

# create figure
fig = matplotlib.pyplot.Figure()

# create matplotlib canvas using `fig` and assign to widget `top_frame`
canvas = FigureCanvasTkAgg(fig, top_frame)

# get canvas as tkinter widget and put in widget `top`
canvas.get_tk_widget().pack()
               
# create toolbar in canvas              
toolbar = NavigationToolbar2Tk(canvas, top_frame)
#toolbar.update() # I'm not sure if it is needed. Code works without it too 

# --- first plot ---

# create first place for plot
ax1 = fig.add_subplot(211)

# draw on this plot
ax1.plot(y1)

# --- second plot ---

# create second place for plot
ax2 = fig.add_subplot(212)

# draw on this plot
ax2.plot(y2)

# --- other widgets in bottom ---

b = tk.Button(bottom_frame, text='Exit', command=root.destroy)
b.pack()

# --- start ----

root.mainloop()

