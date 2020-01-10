#!/usr/bin/env python3 

# date: 2020.01.04
# 

import tkinter as tk

# --- classes ---

class MyCanvas(tk.Canvas):
    
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self._cursorx = self.create_line(0, 0, 0, root.winfo_height())
        self._cursory = self.create_line(0, 0, root.winfo_width(), 0)
        self.bind('<Motion>', self.on_motion)

    def on_motion(self, event):
        x = event.x
        y = event.y
        #self.coords(self._cursorx, x, 0, x, root.winfo_height())
        #self.coords(self._cursory, 0, y, root.winfo_width(), y)
        self.moveto(x, y)

    def moveto(self, x, y):
        self.coords(self._cursorx, x, 0, x, root.winfo_height())
        self.coords(self._cursory, 0, y, root.winfo_width(), y)

# --- main ---

root = tk.Tk()

canvas1 = MyCanvas(root, bg='red')
canvas1.grid(row=0, column=0)

canvas2 = MyCanvas(root, bg='green')
canvas2.grid(row=0, column=1)

canvas3 = MyCanvas(root, bg='blue')
canvas3.grid(row=1, column=0)

canvas4 = MyCanvas(root, bg='yellow')
canvas4.grid(row=1, column=1)

root.mainloop()

