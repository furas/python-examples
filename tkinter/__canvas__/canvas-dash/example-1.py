#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

canvas.create_line(0, 10, 400, 10, dash=(5, 1))
canvas.create_line(0, 20, 400, 20, dash=(5, 5))
canvas.create_line(0, 30, 400, 30, dash=(1, 1))
canvas.create_line(0, 40, 400, 40, dash=(4, 1))
canvas.create_line(0, 50, 400, 50, dash=(5, 10))
canvas.create_line(0, 60, 400, 60, dash=(5, 5, 2, 5))
canvas.create_line(0, 70, 400, 70, dash=(5, 5, 20, 5))

root.mainloop()
