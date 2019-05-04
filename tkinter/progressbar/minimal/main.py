
# date: 2019.05.02
# author: Bartłomiej 'furas' Burek

import tkinter as tk
import tkinter.ttk as ttk

def draw_next_rect():
    progressbar.step()
    if progressbar['value'] < 50:
        master.after(100, draw_next_rect)

master = tk.Tk()

progressbar = ttk.Progressbar(master, maximum=50.001, mode='indeterminate')
progressbar.pack()

draw_next_rect()

master.mainloop()
