#!/usr/bin/env python

#import sys
#
#if sys.version_info.major == 2:
#    import Tkinter as tk
#else:
#    import tkinter as

try:
    import Tkinter as tk # Python 2.x
except:
    import tkinter as tk # Python 3.x    
    
from datetime import datetime


# --- constants ---

    # empty

# --- classes ---

class Clock(tk.Tk):

    def __init__(self):
        # create main window and set its title
        
        tk.Tk.__init__(self) # Python 2 & 3
        #super().__init__() # Python 3 only
        
        self.title('Time')

        # create variable for displayed time and use it with Label
        
        self.txt_var = tk.StringVar()

        tk.Label(self, textvariable=self.txt_var).pack()

    def update(self):
        # update displayed time
        current_time = datetime.now()
        current_time_str = current_time.strftime('%Y.%m.%d  %H:%M:%S')
        # current_time_str = datetime.now().strftime('%Y.%m.%d  %H:%M:%S')
        self.txt_var.set(current_time_str)
        
        # rupdate again after 1000ms (1s)
        self.after(1000, self.update)

    def run(self):
        # update first time
        self.update()
        
        # start the engine :)
        self.mainloop()

# --- functions ---

    # empty

# --- main ---

Clock().run()
