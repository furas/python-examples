#!/usr/bin/env python3

import tkinter as tk # Python 3
    
class App(tk.Tk):
 
    def __init__(self):
        #super(App, self).__init__() # Python 3
        super().__init__() # Python 3
 
        self.title('Main Window')
        self.geometry('300x300')
 
#    def run(self):
#        self.mainloop()
 
#app = App()
#app.run()
 
#App().run()

App().mainloop()
