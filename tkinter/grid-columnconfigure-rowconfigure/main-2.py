#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
