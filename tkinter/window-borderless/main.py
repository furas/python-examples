#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

# set size and position
root.geometry('200x100+500+500')

# create borderless window
root.overrideredirect(True)

# close on mouse click
# (because there is no close button `X` on border)
root.bind('<Button-1>', lambda e:root.destroy())

root.mainloop()
