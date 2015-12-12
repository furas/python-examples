#!/usr/bin/env python

import Tkinter as tk # Python 2
    
class App(tk.Tk):
 
    def __init__(self):
        tk.Tk.__init__(self) # Python 2
        
        self.title('Main Window')
        self.geometry('300x300')
 
#    def run(self):
#        self.mainloop()
 
#app = App()
#app.run()
 
#App().run()

App().mainloop()


