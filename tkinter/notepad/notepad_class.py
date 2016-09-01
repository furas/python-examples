#!/usr/bin/env python

#
# modifications for: http://codeshot.in/pythongui/notepad.php
#
# FB: https://www.facebook.com/groups/learnpython.org/permalink/1180950268636255/
#

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# --- constants ---

    # empty
    
# --- classes ---

class Notepad(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self) # Python 2 & 3
        #super().__init__() # Python 3 only
        
        self.title("Text Editor")

        # add a text box
        self.text = tk.Text(self)
        self.text.pack()

        # menus
        menu = tk.Menu(self)
        self.config(menu=menu)

        # file menu
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File", command=self.open_command)
        file_menu.add_command(label="Save As", command=self.save_command)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_command)

        # edit menu
        edit_menu = tk.Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.dummy)
        edit_menu.add_command(label="Redo", command=self.dummy)
        edit_menu.add_command(label="Cut", command=self.dummy)
        edit_menu.add_command(label="Copy", command=self.dummy)
        edit_menu.add_command(label="Paste", command=self.dummy)

        # help menu
        help_menu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about_command)

    def run(self):
        # start the engine :)
        self.mainloop()
        
    def dummy(self):
        messagebox.showinfo("UPS!", "Function not implemented.")

    def open_command(self):
        file_ = filedialog.askopenfile(mode="r")
        if file_:
            content = file_.read()
            self.text.insert("1.0", content)
            file_.close()

    def save_command(self):
        file_ = filedialog.asksaveasfile(mode="w")
        if file_:
            content = self.text.get("1.0", tk.END+"-1c") # do we need "-1c" ???
            file_.write(content)
            file_.close()

    def exit_command(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.destroy()

    def about_command(self):
        messagebox.showinfo("About", "Text Editor Version 1.0.0 \nCopyright 2016 \nCreator : Abhishek Singh")

# --- functions ---

    # empty
    
# --- main ---

Notepad().run() # or Notepad().mainloop()
