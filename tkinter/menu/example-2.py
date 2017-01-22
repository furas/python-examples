#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def update():
    global counter
    counter += 1
    menu.entryconfig(0, label=('Displayed: %d' % counter))

# --- main ----

counter = 0

# - init -
root = tk.Tk()

# - menu -
menubar = tk.Menu(root)

menu = tk.Menu(menubar, tearoff=0, postcommand=update)
menu.add_command(label=str(counter))
menu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label="Test", menu=menu)

root.config(menu=menubar)

# - start -
root.mainloop()
