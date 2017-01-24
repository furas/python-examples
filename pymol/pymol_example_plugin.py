#!/usr/bin/env python2

# plugin file name can't have `-`

import Tkinter as tk
import tkMessageBox
import pymol

class ExamplePlugin:

    def __init__(self, parent):
        self.parent = parent

        # window
        self.root = tk.Toplevel(self.parent)
        self.root.title('Example Plugin')

        # frames
        self.frame = tk.Frame(self.root, padx=5, pady=5, bg='red')
        self.frame.pack()

        # checkbuttons
        self.var = tk.IntVar()

        self.button = tk.Checkbutton(self.frame, text='Select',
                            variable=self.var, command=self.toggle)
        self.button.pack()

    def toggle(self):

        if self.var.get():
          text = "selected"
        else:
          text = "unselected"

        tkMessageBox.showinfo("Selection status", text)

def showWindow():
    # it can work without `parent` but it gives access to parent window
    parent = pymol.plugins.get_tk_root()
    ExamplePlugin(parent)

def __init__(self):
    self.menuBar.addmenuitem("Plugin", "command", label="Example Plugin", command=showWindow)
    # command in `PyMOL>`
    pymol.cmd.extend("ExamplePlugin", showWindow)
    # works in window `Viewer`
    pymol.cmd.set_key("CTRL-F", showWindow)
