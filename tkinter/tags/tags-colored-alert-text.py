#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

txt = tk.Text(root)
txt.pack()

txt.tag_config('warning', background="yellow", foreground="red")

txt.insert('end', "Hello\n")
txt.insert('end', "Alert #1\n", 'warning')
txt.insert('end', "World\n")
txt.insert('end', "Alert #2\n", 'warning')

root.mainloop()
