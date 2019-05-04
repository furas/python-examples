
# date: 2019.05.02
# author: Bartłomiej 'furas' Burek

import tkinter as tk

def draw_next_rect(x):
    w.create_rectangle(0, 100, x*10, 150, fill="#007700")
    x = x+1
    # stop animation if x==51
    if x < 51:
        master.after(100, draw_next_rect, x)

master = tk.Tk()
w = tk.Canvas(master, width=500, height=500)
w.pack()

w.create_rectangle(0, 100, 500, 150, fill="#770077")

# start animation with x=0
draw_next_rect(0)

master.mainloop()
