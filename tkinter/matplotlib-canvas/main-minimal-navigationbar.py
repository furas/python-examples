#!/usr/bin/env python3

import matplotlib 
#import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,    # not FigureCanvasTk
    NavigationToolbar2Tk  # not NavigationToolbar2TkAgg
)
import tkinter as tk

# --- random data ---

import random

y = [random.randint(-100, 100) for x in range(200)]

# --- GUI ---

root = tk.Tk()

#fig = plt.Figure()
fig = Figure()

canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().pack()
               
navbar = NavigationToolbar2Tk(canvas, root)
#navbar.update() # not needed

#ax = fig.add_subplot(111)
ax = fig.subplots()
ax.plot(y)

root.mainloop()

