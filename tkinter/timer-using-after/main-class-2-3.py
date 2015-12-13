#!/usr/bin/env python

try:
    import Tkinter as tk # python 2.x
except:
    import tkinter as tk # python 3.x
    
from datetime import datetime


class Time(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title('Time')

        self.txt = tk.StringVar()

        tk.Label(self, textvariable=self.txt).pack()

    def timer(self):
        self.txt.set(datetime.now().strftime('%Y.%m.%d  %H:%M:%S'))
        # run timer after 1000ms (1s)
        self.after(1000, self.timer)

    def run(self):
        # run timer
        self.timer()
        self.mainloop()

Time().run()
