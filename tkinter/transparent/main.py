#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

root.wait_visibility(root)
root.wm_attributes('-alpha',0.7) # Linux
root.attributes('-alpha',0.7) # Windows ???

tk.Button(root, text='OK').place(x=75, y=75)

root.mainloop()
