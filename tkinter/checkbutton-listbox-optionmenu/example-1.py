#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def on_button():

    # - OptionMenus -
    for i, var in enumerate(o_vars):
        print('OptionMenu {}: {}'.format(i, var.get()))

    print('-------------------------')

    # - Listbox -
    print('ListBox:', l.curselection())
    for i in l.curselection():
        print('option:', OPTIONS[i])

    print('-------------------------')

    # - Checkbuttons -
    print('ChecboxBox:')
    for i, var in enumerate(cb_vars):
        if var.get():
            print('option:', OPTIONS[i])

    print('=========================')

# --- main ---

OPTIONS = ["Script 1", "Script 2", "Script 3", "Script 4", "Script 5"]

root = tk.Tk()

# - OptionMenu -

tk.Label(root, text='OptionMenus', bg='#aaa').pack(fill='x')

o_vars = []

for i in range(3):
    var = tk.StringVar(value='- select -')
    o_vars.append(var)
    tk.OptionMenu(root, var, *OPTIONS).pack()

# - Listbox -

tk.Label(root, text='Listbox', bg='#aaa').pack(fill='x')

l = tk.Listbox(root, selectmode='multiple')
l.pack()
l.insert('end', *OPTIONS)

# - Checkbuttons -

tk.Label(root, text='Checkbuttons', bg='#aaa').pack(fill='x')

cb_vars = []

for option in OPTIONS:
    var = tk.BooleanVar(value=False)
    cb_vars.append(var)
    tk.Checkbutton(root, text=option, variable=var).pack()

# - Button -

b = tk.Button(root, text='OK', command=on_button)
b.pack(fill='x')

# - start -

root.mainloop()
