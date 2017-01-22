#!/usr/bin/env python3

import tkinter as tk

def test(event):
    print('      char:', event.char)
    print('   keycode:', event.keycode)
    print('    keysym:', event.keysym)
    print('keysym_num:', event.keysym_num)
    print('       num:', event.num)
    print('     state:', event.state)
    print('    serial:', event.serial)
    print('send_event:', event.send_event)
    print('      time:', event.time)
    print('      type:', event.type)
    print('---')

root = tk.Tk()

root.bind('<Key>', test)

root.mainloop()
