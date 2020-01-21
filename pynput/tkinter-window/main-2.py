#!/usr/bin/env python3

# date: 2020.01.20
# ???

import tkinter as tk
from pynput.keyboard import Listener, Key

# --- functions ---

def onpress(key): # `key` can be `Key` (which doesn't have `char`) or `KeyCode` (which have `char`)
    global listen 

    print(str(key) == "'1'", str(key))

    #if key == Key.esc:
    if str(key) == 'Key.esc':
        listen = not listen

    if listen:
        #if hasattr(key, 'char') and key.char == '1': # there is no `Key.1` and `1` 
        if str(key) == "'1'": # it need `' '` in string
            label_var.set(label_var.get()+'1')
            print('1!')

# --- main ---

listen = False

root = tk.Tk()

label_var = tk.StringVar()

label = tk.Label(root, textvariable=label_var, width=10)
label.pack()

listener = Listener(on_press=onpress)
print('start')
listener.start()
try:
    listener.wait()
    print('mainloop')
    root.mainloop()
finally:
    print('stop')
    listener.stop()
    print('end')
    # without `listener.join()` because it runs as `daemon`
    
