#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
#root.geometry('300x300')

#root.columnconfigure(1, minsize=100)
#root.columnconfigure(3, minsize=100)
#root.rowconfigure(1, minsize=100)
#root.rowconfigure(3, minsize=100)

#root.columnconfigure(1, weight=0)
#root.columnconfigure(3, weight=2)
#root.rowconfigure(1, weight=1)
#root.rowconfigure(3, weight=1)

b = tk.Button(root, text="Exit", command=root.destroy)
b.grid(column=2, row=2)

root.mainloop()
