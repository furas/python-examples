#!/usr/bin/env python3

import tkinter as tk

def copy(event):
    print('copy')
    
def paste(event):
    print('paste')
    
def test(event):    
    print('   char:', event.char)
    print('keycode:', event.keycode)
    print(' keysym:', event.keysym)
    print('---')


root = tk.Tk()

# english
#root.bind('<Control-c>', copy)
#root.bind('<Control-v>', paste)

# russian - doesn't work, tkinter use english keys
root.bind('<Control-Cyrillic_es>', copy)
root.bind('<Control-Cyrillic_em>', paste)

# test
root.bind('<Key>', test)

root.mainloop()
