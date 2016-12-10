#!/usr/bin/env python3

import tkinter as tk

def test(event):    
    print('   char:', event.char)
    print('keycode:', event.keycode)
    print(' keysym:', event.keysym)
    print('---')

root = tk.Tk()

root.bind('<Key>', test)

root.mainloop()
