#!/usr/bin/env python3

# date: 2019.10.14
# 

import tkinter as tk

class VRuler(tk.Canvas):
    '''Vertical Ruler'''
    
    def __init__(self, master, width, height, offset=0):
        super().__init__(master, width=width, height=height)
        self.offset = offset

        step = 10

        # start at `step` to skip line for `0`
        for y in range(step, height, step):
            if y % 50 == 0:
                # draw longer line with text
                self.create_line(0, y, 13, y, width=2)
                self.create_text(20, y, text=str(y), angle=90)
            else:
                self.create_line(2, y, 7, y)
                
        self.position = self.create_line(0, 0, 50, 0, fill='red', width=2)

    def set_mouse_position(self, y):
        y -= self.offset
        self.coords(self.position, 0, y, 50, y) 
        
class HRuler(tk.Canvas):
    '''Horizontal Ruler'''
    
    def __init__(self, master, width, height, offset=0):
        super().__init__(master, width=width, height=height)
        self.offset = offset
        
        step = 10

        # start at `step` to skip line for `0`
        for x in range(step, width, step):
            if x % 50 == 0:
                # draw longer line with text
                self.create_line(x, 0, x, 13, width=2)
                self.create_text(x, 20, text=str(x))
            else:
                self.create_line((x, 2), (x, 7))
                
        self.position = self.create_line(0, 0, 0, 50, fill='red', width=2)

    def set_mouse_position(self, x):
        x -= self.offset
        self.coords(self.position, x, 0, x, 50) 

def motion(event):
    x, y = event.x, event.y
    hr.set_mouse_position(x)
    vr.set_mouse_position(y)

def click(event):
    print(event.x, event.y)
    
root = tk.Tk()
root['bg'] = 'black'

vr = VRuler(root, 25, 250)#, offset=25)
vr.place(x=0, y=28)

hr = HRuler(root, 250, 25)#, offset=25)
hr.place(x=28, y=0)

c = tk.Canvas(root, width=250, height=250)
c.place(x=28, y=28)

#root.bind('<Motion>', motion) # it needs offset=28 if there is no Canvas
c.bind('<Motion>', motion)
c.bind('<Button-1>', click)

root.mainloop()

