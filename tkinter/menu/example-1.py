#!/usr/bin/env python3

import tkinter as tk

# --- functions ---

def callback(event=None):
    print('Menu:File')
    print('Menu:File:Check 1:', var_check_1.get(), type(var_check_1.get()))
    print('Menu:File:Check 2:', var_check_2.get(), type(var_check_2.get()))
    print('Menu:File:Radio  :', var_radio.get(), type(var_radio.get()))

# --- main ----

# - init -
root = tk.Tk()

var_check_1 = tk.StringVar()
var_check_2 = tk.StringVar(value="second is ON")
var_radio = tk.IntVar(value=102)

# - menu -
menubar = tk.Menu(root)

menu_file = tk.Menu(menubar, tearoff=False)

menu_file.add_command(label='Open', command=callback, accelerator='Ctrl+O')
menu_file.add_command(label='Save', command=callback)
menu_file.add_command(label='Close', command=callback)
menu_file.add_separator()
menu_file.add_checkbutton(label='Check #1', command=callback, variable=var_check_1, onvalue="first is ON", offvalue="first is OFF")
menu_file.add_checkbutton(label='Check #2', command=callback, variable=var_check_2, onvalue="second is ON", offvalue="second is OFF")
menu_file.add_separator()
menu_file.add_radiobutton(label='Radio #0', command=callback, variable=var_radio, value=100)
menu_file.add_radiobutton(label='Radio #1', command=callback, variable=var_radio, value=101)
menu_file.add_radiobutton(label='Radio #2', command=callback, variable=var_radio, value=102)
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.destroy)

menubar.add_cascade(label='File', menu=menu_file)

root.config(menu=menubar)

root.bind('<Control-o>', callback)

# - popup menu -

def show_popup(event):
    popup_menu.post(event.x_root, event.y_root)

popup_menu = tk.Menu(root, tearoff=False)
popup_menu.add_command(label='Option 1', command=callback)
popup_menu.add_command(label='Option 2', command=callback)
root.bind('<Button-3>', show_popup)

# - start -
root.mainloop()
