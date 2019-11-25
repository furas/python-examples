#!/usr/bin/env python3 

# date: 2019.11.23
# https://stackoverflow.com/questions/59003443/how-can-i-trigger-a-button-by-painting-over-it-using-tkinters-b1-motion

import tkinter as tk

class PaintOverWidget():

    def __init__(self, master):
        self.b = tk.Button(master, text="UnMark All", command=self.clicked)
        self.b.bind("<B1-Motion>", self.pressed)
        master.bind("<B1-Motion>", self.pressed2)
        self.b.pack()

    def clicked(self):
        print('clicked')

    def pressed(self, event):
        print('painted')

    def pressed2(self, event):
        bx1 = self.b.winfo_rootx()
        bx2 = bx1 + self.b.winfo_width()
        by1 = self.b.winfo_rooty()
        by2 = by1 + self.b.winfo_height()
        if (bx1 <= event.x_root <= bx2) and (by1 <= event.y_root <= by2):
            print('painted 2')
            return 'break'
        
root = tk.Tk()
my_gui = PaintOverWidget(root)
root.mainloop()
