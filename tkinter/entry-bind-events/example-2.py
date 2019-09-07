#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_press(event, text):
    print('  press:', text)
    #print('  event:', event)
    #print(' widget:', event.widget)
    print('   char:', event.char)
    #print('   char:', event.code)

def on_release(event, text):
    print('release:', text)
    #print('  event:', event)
    #print(' widget:', event.widget)
    print('   char:', event.char)
    #print('   char:', event.code)

def on_return(event):
    on_press(event, 'return')

def on_return_release(event):
    on_release(event, 'return')

def on_key(event):
    on_press(event, 'any key')

def on_key_release(event):
    on_release(event, 'any key')

def on_ctrl_a(event):
    on_press(event, 'Ctrl+a')

def on_ctrl_a_release(event):
    on_release(event, 'Ctrl+a')

def on_combo_1(event):
    on_press(event, 'Combo 1')

def on_combo_2(event):
    on_press(event, 'Combo 2')

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
e.bind('<space>a', on_combo_2)

root.mainloop()

