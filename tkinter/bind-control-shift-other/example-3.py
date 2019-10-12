#!/usr/bin/env python3

# date: 2019.09.28
# https://stackoverflow.com/questions/58147952/tkinter-how-to-bind-just-control-not-controlkey

# You would have to bind <Control_L> and <Control_R>

import tkinter as tk

def on_press(event):
    print(event)

root = tk.Tk()
root.bind('<Control_L>', on_press)
root.bind('<Control_R>', on_press)
root.mainloop()

# Eventually you can use <Key> which is executed with every key and then check event.keysym or event.code

import tkinter as tk

def on_press(event):
    print(event)
    print(event.keysym in ('Control_L', 'Control_R'))
    print(event.keycode in (37, 105))

root = tk.Tk()
root.bind('<Key>', on_press)
root.mainloop()
