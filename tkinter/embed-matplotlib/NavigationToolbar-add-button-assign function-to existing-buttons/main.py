
# date: 2019.04.07
# https://matplotlib.org/gallery/user_interfaces/embedding_in_tk_sgskip.html

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

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

# add button to NavigationToolbar2Tk
button = tkinter.Button(master=toolbar, text="Quit", command=_quit)
#button.pack()
button.pack(side="left")

def my_function():
    print("Left Arrow")

# add function to button with left arrow
toolbar.children['!button2'].config(command=my_function)

#for item in toolbar.children: print(item) # print(item.config())

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
