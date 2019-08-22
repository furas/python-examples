#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_return(event):
    print('press  : return', event.widget.get())
    #print('e.get():', e.get())

def on_return_release(event):
    print('release: return', event.widget.get())
    #print('e.get():', e.get())

def on_key(event):
    print('press  : any key', event.widget.get())

def on_key_release(event):
    print('release: any key', event.widget.get())

def on_ctrl_a(event):
    print('on Ctrl+a (press)  :', event.widget.get())

def on_ctrl_a_release(event):
    print('on Ctrl+a (release):', event.widget.get())

def on_combo_1(event):
    print('on Combo 1:', event.widget.get())

def on_press(event, text):
    print('press :', text) #, event.widget.get())

def on_release(event, text):
    print('release:', text) #, event.widget.get())

# --- main ---

root = tk.Tk()

e = tk.Entry(root)
e.pack()


# button Enter/Return so you don't need tk.Button
e.bind('<Return>', on_return)

# button Enter/Return so you don't need tk.Button
e.bind('<KeyRelease-Return>', on_return_release)

# Key/KeyPress is executed before last key is putted in Entry
e.bind('<Key>', on_key)
#e.bind('<KeyPress>', on_key)

# KeyRelease is executed after last key is putted in Entry
e.bind('<KeyRelease>', on_key_release)

# keys combination - at the same time
e.bind('<Control-a>', on_ctrl_a)

# keys combination - at the same time
e.bind('<Control-KeyRelease-a>', on_ctrl_a_release)

# keys combination - you can press one after another
e.bind('<Control-Key>a', on_combo_1)

# keys combination - you can press one after another
e.bind('<space>a', on_combo_1)

root.mainloop()

