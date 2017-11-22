#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

# keep selected value (and connect radiobuttons)
v = tk.IntVar()

# use the same `variable`
r1 = tk.Radiobutton(root, text="Radiobutton 1", variable=v, value=1, indicatoron=0)
r2 = tk.Radiobutton(root, text="Radiobutton 2", variable=v, value=2, indicatoron=0)
r3 = tk.Radiobutton(root, text="Radiobutton 3", variable=v, value=3, indicatoron=0)
r4 = tk.Radiobutton(root, text="Radiobutton 4", variable=v, value=4, indicatoron=0)

# make them look like buttons (fill space, use internal padding)
r1.pack(fill='both', ipady=5, ipadx=30)
r2.pack(fill='both', ipady=5, ipadx=30)
r3.pack(fill='both', ipady=5, ipadx=30)
r4.pack(fill='both', ipady=5, ipadx=30)

# normal button to reset radiobuttons 
b = tk.Button(root, text='Reset', command=lambda:v.set(0))
b.pack(fill='both', pady=(10,0)) # extra space above button

root.mainloop()
