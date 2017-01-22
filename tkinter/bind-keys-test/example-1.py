#!/usr/bin/env python3

import tkinter as tk

def pressed(text, event=None):
    print('text:', text)
    if event:
        print(dir(event))
        print('char:', event.char)
        print('keycode:', event.keycode)
        print('keysym:', event.keysym)
        print('keysym_num:', event.keysym_num)
        print('num:', event.num)
        print('state:', event.state)
        print('serial:', event.serial)
        print('send_event:', event.send_event)
        print('time:', event.time)
        print('type:', event.type)


def hello(event=None):
    print("Hello")

root = tk.Tk()

root.bind('<Control-m>', lambda event:pressed('Ctrl+m', event))
root.bind('<Alt-m>', lambda event:pressed('Alt+m', event))
root.bind('<M>', lambda event:pressed('Shift+m', event))
root.bind('<m>', lambda event:pressed('m', event))
root.bind('hi', hello)

root.mainloop()
