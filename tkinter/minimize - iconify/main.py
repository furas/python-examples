#!/usr/bin/env python3

# date: 2020.06.27

import tkinter as tk

root = tk.Tk()

# button [X] minimize (iconify) the main window
root.protocol("WM_DELETE_WINDOW", root.iconify)

# key ESC  minimize (iconify) the main window
#root.bind('<Escape>', lambda event: root.destroy())
root.bind('<Escape>', lambda event: root.iconify())

# create a menu bar with an `Exit` and `Hide`
menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Hide", command=root.iconify)
filemenu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
