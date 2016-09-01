#!/usr/bin/env python

#
# modifications for: http://codeshot.in/pythongui/notepad.php
#
# FB: https://www.facebook.com/groups/learnpython.org/permalink/1180950268636255/
#

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# --- functions ---

def dummy():
    messagebox.showinfo("UPS!", "Function not implemented.")

def open_command():
    file_ = filedialog.askopenfile(mode="r")
    if file_:
        content = file_.read()
        text.insert("1.0", content)
        file_.close()

def save_command():
    file_ = filedialog.asksaveasfile(mode="w")
    if file_:
        content = text.get("1.0", tk.END+"-1c") # do we need "-1c" ???
        file_.write(content)
        file_.close()

def exit_command():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        master.destroy()

def about_command():
    messagebox.showinfo("About", "Text Editor Version 1.0.0 \nCopyright 2016 \nCreator : Abhishek Singh")

# --- main ---

master = tk.Tk()
master.title("Text Editor")

# add a text box
text = tk.Text(master)
text.pack()

# menus
menu = tk.Menu(master)
master.config(menu=menu)

# file menu
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=open_command)
file_menu.add_command(label="Save As", command=save_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_command)

# edit menu
edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=dummy)
edit_menu.add_command(label="Redo", command=dummy)
edit_menu.add_command(label="Cut", command=dummy)
edit_menu.add_command(label="Copy", command=dummy)
edit_menu.add_command(label="Paste", command=dummy)

# help menu
help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_command)

# start the engine :)
master.mainloop()
