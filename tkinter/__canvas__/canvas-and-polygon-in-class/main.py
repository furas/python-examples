#!/usr/bin/env python

# http://stackoverflow.com/questions/33855618/how-to-configure-a-polygon-on-a-tkinter-canvas-in-python-using-a-class

try:
    import Tkinter as tk # python 2
except:
    import tkinter as tk # python 3


# --- class ---

class GUI(tk.Canvas):
    '''
    Inherits Canvas class (all Canvas methodes, attributes will be accessible)
    You can add your customized methods here.
    '''
    
    def __init__(self,master,*args,**kwargs):
        tk.Canvas.__init__(self, master=master, *args, **kwargs)
        self.poly = None

    def create_poly(self, points, outline='gray', fill='gray', width=2):
        self.poly = self.create_polygon(points, outline=outline, fill=fill, width=width)
                    
    def set_poly_fill(self, color):
        if self.poly:
            self.itemconfig(self.poly, fill=color)

# --- main ---
    
root = tk.Tk()

polygon = GUI(root)
polygon.create_poly( [150,75,225,0,300,75,225,150] )
polygon.set_poly_fill('red')
polygon.pack()

root.mainloop()
