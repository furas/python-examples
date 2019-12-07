#!/usr/bin/env python3 

# date: 2019.12.03
# https://stackoverflow.com/questions/59155873/how-to-remove-toolbar-button-from-navigationtoolbar2tk-figurecanvastkagg

import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# ---

# remove button `Pan` from toolbar
NavigationToolbar2Tk.toolitems = [t for t in NavigationToolbar2Tk.toolitems if
                 t[0] not in ('Pan',)]

# ---

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

print(toolbar.toolitems)

# ---


toolbar.children['!button4'].pack_forget()

# --- 
#To remove Pan button - it is 4th button

toolbar.children['!button4'].pack_forget()

#To assign new function to existing button - ie. Home

def my_function():
    print("Pressed Home")

toolbar.children['!button1'].config(command=my_function)

# ---

canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

label = tkinter.Button(master=root, text="Label")
label.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
