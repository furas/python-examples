#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_change():
    print('Boolean:', var_bool.get(), type(var_bool.get()))
    print('Integer:', var_int.get(),  type(var_int.get()))
    print(' String:', var_str.get(),  type(var_str.get()))

# --- main ---

root = tk.Tk()

# --------------------

# Boolean can have    True/False, 
# IntVar can have     1/0
# StringVar can have "1"/"0"/""

# --------------------

#var_bool = tk.BooleanVar(value=False) # set value at start
var_bool = tk.BooleanVar() # default value False

#tk.Checkbutton(root, text='OK', variable=var, command=on_change).pack()
cb = tk.Checkbutton(root, text='Boolean', variable=var_bool, command=on_change)
cb.pack()

# change value at any moment and it changes Checkbutton
var_bool.set(True)  # any integer number ; string only: "0", "1" ; bolean: True, False 

# --------------------

#var_int = tk.IntVar(value=1) # set value at start
var_int = tk.IntVar() # default value 0

#tk.Checkbutton(root, text='OK', variable=var, command=on_change).pack()
cb = tk.Checkbutton(root, text='Integer', variable=var_int, command=on_change)
cb.pack()

# change value at any moment and it changes Checkbutton
var_int.set(2)  # any integer number ; string only: "0", "1" ; bolean: True, False 

# --------------------

#var_str = tk.StringVar(value="1")
#var_str = tk.StringVar(value=1)
var_str = tk.StringVar() # default value - empty string - special effect

cb = tk.Checkbutton(root, text='String', variable=var_str, command=on_change)
cb.pack()

#var_str.set(1) 
var_str.set("a") 
# 1, "1" - checked
# 0, "0", any non-empty string - unchecked
# "" (empty string) - chceked and grayed

# --------------------

root.mainloop()
