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
    
from datetime import datetime, timedelta


# --- constants ---

    # empty

# --- classes ---

class Clock(tk.Frame):

    def __init__(self, parent, offset_minutes=0):
        # create widget (and send all arguments to Frame, ie. parent)
        
        tk.Frame.__init__(self, parent) # Python 2 & 3
        #super().__init__() # Python 3 only

        self.offset_minutes = timedelta(minutes=offset_minutes)
        
        # create variable for displayed time and use it with Label
        
        self.txt_var = tk.StringVar()

        tk.Label(self, textvariable=self.txt_var).pack()

    def update_time(self):
        # update displayed time
        current_time = datetime.now()
        current_time += self.offset_minutes
        current_time_str = current_time.strftime('%Y.%m.%d  %H:%M:%S')
        # current_time_str = datetime.now().strftime('%Y.%m.%d  %H:%M:%S')
        self.txt_var.set(current_time_str)
        
        # run update_time again after 1000ms (1s)
        self.after(1000, self.update_time)

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('World Times')
        
        tk.Label(self, text="Local:").grid(row=0, column=0, sticky=tk.E)
        tk.Label(self, text="+120min.:").grid(row=1, column=0, sticky=tk.E)
        
        self.clock_1 = Clock(self)
        self.clock_1.grid(row=0, column=1)
        
        self.clock_2 = Clock(self, 120)
        self.clock_2.grid(row=1, column=1)

    def run(self):
        # run update_time first time
        self.clock_1.update_time()
        self.clock_2.update_time()
        
        # start the engine :)
        self.mainloop()

        
# --- functions ---

    # empty

# --- main ---

App().run()
