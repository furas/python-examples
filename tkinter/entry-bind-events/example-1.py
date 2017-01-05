#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_return(event):
    print('on return:', event.widget.get())
    #print('e.get():', e.get())

def on_key(event):
    print('on key:', event.widget.get())

def on_key_release(event):
    print('on key release:', event.widget.get())

def on_ctrl_a(event):
    print('on Ctrl+a:', event.widget.get())

def on_combo_1(event):
    print('on Combo 1:', event.widget.get())

# --- main ---

root = tk.Tk()

e = tk.Entry(root)
e.pack()


# button Enter/Return so you don't need tk.Button
e.bind('<Return>', on_return)

# Key/KeyPress is exeecuted before last key is putted in Entry
#e.bind('<Key>', on_key)
e.bind('<KeyPress>', on_key)

# KeyRelease is exeecuted after last key is putted in Entry
e.bind('<KeyRelease>', on_key_release)

# keys combination - at the same time
e.bind('<Control-a>', on_ctrl_a)

# keys combination - you can press one after another
e.bind('<space>a', on_combo_1)


root.mainloop()

