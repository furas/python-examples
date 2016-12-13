#!/usr/bin/env python3

#
# http://matplotlib.org/examples/user_interfaces/embedding_in_tk.html
#

# --- matplotlib ---
import matplotlib 
matplotlib.use('TkAgg') # choose backend

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.pyplot import Figure

# --- other ---
import tkinter as tk
import pandas as pd

# --- for example data --
import random
import math

# --- random data ---

df1 = pd.DataFrame([random.randint(-100, 100) for _ in range(60)])
df2 = pd.DataFrame([math.sin(math.radians(x*6)) for x in range(60)])

# --- GUI ---

root = tk.Tk()

# top frame for canvas and toolbar - which need `pack()` layout manager
top = tk.Frame(root)
top.pack()

# bottom frame for other widgets - which may use other layout manager 
bottom = tk.Frame(root)
bottom.pack()

# --- canvas and toolbar in top ---

# create figure
fig = matplotlib.pyplot.Figure()

# create matplotlib canvas using `fig` and assign to widget `top`
canvas = FigureCanvasTkAgg(fig, top)

# get canvas as tkinter widget and put in widget `top`
canvas.get_tk_widget().pack()
               
# create toolbar               
toolbar = NavigationToolbar2TkAgg(canvas, top)
toolbar.update()
canvas._tkcanvas.pack()

# --- first plot ---

# create first place for plot
ax1 = fig.add_subplot(211)

# draw on this plot
df1.plot(kind='bar', legend=False, ax=ax1)

# --- second plot ---

# create second place for plot
ax2 = fig.add_subplot(212)

# draw on this plot
df2.plot(kind='bar', legend=False, ax=ax2)

# --- other widgets in bottom ---

b = tk.Button(bottom, text='Exit', command=root.destroy)
b.pack()

# --- start ----

root.mainloop()
