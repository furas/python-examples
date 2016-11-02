#!/usr/bin/env python3

import tkinter as tk

def on_change(event=None):
    if event:
        print('--- bind ---')
        print(' event:', event)
        print('widget:', event.widget)
        print(' value:', event.widget.get())
        event.widget.delete(0, 'end');
        event.widget.insert(0, '13') 
    else:
        print('--- command ---')
        print('widget:', sb)
        print(' value:', sb.get())
        

root =tk.Tk()

sb = tk.Spinbox(root, from_=10, to_=20, command=on_change)
sb.pack()
sb.bind('<Return>', on_change)
sb.bind('<Key>', on_change)
#sb.bind('<<Change>>', on_change) # doesn't work


root.mainloop()
