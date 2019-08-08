
# 2019.08.05
# 
# Button runs function which gets text from Entry but it has no method to get 
# this value if function use `return text`. Function has to assign value 
# to global variable to use this value later outside function 
# (or after closing window)

import tkinter as tk

# --- functions ---

def get_name():
    global name # inform function to use global variable instead of creating local one
    
    name = name_entry.get() # assign value to global variable

    root.destroy() # closing window

# --- main ---

name = ''  # global variable with default value (if you don't put name)

root = tk.Tk()

name_label = tk.Label(root, text='Name')
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack(side='right')

b = tk.Button(root, text='First', command=get_name)
b.pack(side='right')

root.mainloop()

print('name:', name) # use value from global varaible after closing window
