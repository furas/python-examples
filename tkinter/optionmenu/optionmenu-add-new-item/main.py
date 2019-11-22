#!/usr/bin/env python3 

# date: 2019.11.07
# 

import tkinter as tk

# --- functions ---

def add_to_list():
    
    text = entry.get()
    
    if text not in category_list:
        category_list.append(text)

        option_var.set('')

        menu = option['menu']
        menu.add_command(label=text, command=tk._setit(option_var, text, on_select))
                              
def on_select(selection):
    print('var:', option_var.get())
    print('sel:', selection)

# --- main ---

category_list = ['Option A', 'Option B','Option C']


root = tk.Tk()

option_var = tk.StringVar()

option = tk.OptionMenu(root, option_var, *category_list, command=on_select)
option.grid(column=0, row=0)

entry = tk.Entry(root)
entry.grid(column=1, row=0)

button = tk.Button(root, text='Add To List', command=add_to_list)
button.grid(column=2, row=0)

root.mainloop()


