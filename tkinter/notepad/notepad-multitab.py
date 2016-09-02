#!/usr/bin/env python

#
# modifications for: http://codeshot.in/pythongui/notepad.php
#
# FB: https://www.facebook.com/groups/learnpython.org/permalink/1180950268636255/
#

import os # os.path.basename
import tkinter as tk
from tkinter import ttk 
from tkinter import filedialog
from tkinter import messagebox

# --- constants ---

    # empty
    
# --- classes ---

class Document(tk.Text):
    
    def __init__(self, master, filename=None):
        super().__init__(master) # Python 3 only

        self.filename = filename
        
        # on Linux background is not white
        self.config(bg='white')

    def debug(self):
        print(self.master, self.master.tab(0))
        
    def save(self):
        if not self.filename:
            
class Notepad(tk.Tk):

    def __init__(self):
        super().__init__() # Python 3 only

        self.create_GUI()
        
        self.docs = [] # keep documents

        doc = Document(self.tabs)
    
        self.docs.append(doc)
        self.tabs.add(doc, text='noname')

    def create_GUI(self):

        self.geometry('800x600')
        
        self.title("TkNotes")

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(fill=tk.BOTH, expand=True)

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
            # get file name
            name = os.path.basename(file_.name)
            
            doc = Document(self.tabs)
        
            content = file_.read()
            doc.insert("1.0", content)
            file_.close()

            self.docs.append(doc)
            self.tabs.add(doc, text=name)

    def save_command(self):
        file_ = filedialog.asksaveasfile(mode="w")
        if file_:
            content = self.text.get("1.0", tk.END) # tk.END+"-1c" # do we need "-1c" ???
            file_.write(content)
            file_.close()

    def exit_command(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.destroy()

    def about_command(self):
        messagebox.showinfo("About", "TkNotes 0.1\nBartłomiej \"furas\" Burek\nCopyright 2016")

# --- functions ---

    # empty
    
# --- main ---

Notepad().run() # or Notepad().mainloop()
