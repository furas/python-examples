#!/usr/bin/env python3 

# date: 2019.12.21
# 

import multiprocessing
import time
import tkinter.ttk as ttk
#from tkinter import * # not preferred
import tkinter as tk

class SubWindow:
    
    def __init__(self, master):
        self.master = master

        self.win = tk.Toplevel(master)
        #self.win.wm_attributes('-topmost', 1)
        
        l = tk.Label(self.win, text='Please, wait...')
        l.pack()

        self.pb = ttk.Progressbar(self.win, mode="determinate")
        self.pb.pack()
        
        self.queue = multiprocessing.Queue()
        
        self.p = multiprocessing.Process(target=self.process, args=(self.queue,))
        self.p.start()
        #p.join() # don't use in this place becaus it blocks all code

        self.update_progressbar()

    def update_progressbar(self):
        if not self.queue.empty():
            self.pb['value'] += self.queue.get()
            
        if self.pb['value'] < 100:
            self.win.after(100, self.update_progressbar)
        else:
            self.p.join()
            self.win.destroy()
            
    def process(self, queue):
        for i in range(10):
            print('loop:', i)
            queue.put(10)
            time.sleep(.5)


if __name__ == "__main__":
    root = tk.Tk()
    tk.Button(root, text='Start processing!', command=lambda:SubWindow(root)).pack(side='top')
    root.mainloop()
