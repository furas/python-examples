#!/usr/bin/env python

import sys


if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
    
from datetime import datetime


class Time(tk.Tk):

    def __init__(self):
        #~ if sys.version_info.major == 2:
        tk.Tk.__init__(self)
        #~ else:
            #~ super().__init__()
        
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
