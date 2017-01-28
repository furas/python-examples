#!/usr/bin/env python2

# plugin can't have `-` in filename
# `pymol-example-plugin.py` will not work
# `pymol_example_plugin.py` will work

import Tkinter as tk
import tkMessageBox
import pymol

class ExamplePlugin:

    def __init__(self, parent):

        self.parent = parent

        # window
        win = tk.Toplevel(self.parent)
        win.title('Example Plugin')

        # label
        b = tk.Label(win, text='Select option')
        b.pack()

        # checkbuttons
        self.var = tk.IntVar()

        self.cb = tk.Checkbutton(win, text='OFF', indicatoron=0, variable=self.var, command=self.toggle)
        self.cb.pack()

        # button
        b = tk.Button(win, text='Close', command=win.destroy)
        b.pack()

    def toggle(self):

        if self.var.get():
            text = 'selected'
            # change text on checkbutton
            self.cb['text'] = 'ON'
        else:
            text = 'unselected'
            # change text on checkbutton
            self.cb['text'] = 'OFF'

        tkMessageBox.showinfo('Selection status', text)

def show():
    # it can work without `parent`
    # but `parent` may give access to parent window
    # (but I don't know if it is usefull)
    parent = pymol.plugins.get_tk_root()
    ExamplePlugin(parent)

def __init__(self):
    # add to menu `Plugin`
    self.menuBar.addmenuitem('Plugin', 'command', label='Example Plugin', command=show)

    # create command 'ExamplePlugin' for `PyMOL>`
    pymol.cmd.extend('ExamplePlugin', show)

    # create shortcut which works in `Viewer`
    pymol.cmd.set_key('CTRL-F', show)

    # show plugin window at start (if you need it)
    show()
