#!/usr/bin/env python3

# --- Python 3 ---
import tkinter as tk
#from tkinter import ttk

#import tkinter.scrolledtext as tkscrolledtext
#import tkinter.colorchooser as tkcolorchooser
#import tkinter.commondialog as tkcommondialog
#import tkinter.filedialog as tkfiledialog
#import tkinter.font as tkfont
#import tkinter.messagebox as tkmessagebox
#import tkinter.simpledialog as tksimpledialog

# --- Python 2 ---
#import Tkinter as tk
#import ttk

#import ScrolledText as tkscrolledtext
#import tkColorChooser as tkcolorchooser
#import tkCommonDialog as tkcommondialog
#import tkFileDialog as tkfiledialog
#import tkFont as tkfont
#import tkMessageBox as tkmessagebox
#import tkSimpleDialog as tksimpledialog

# --- common ---
#from PIL import Image, ImageTk

# --- functions ---

def callback():
    print('callback')

# --- main ---

root = tk.Tk()

#var = tk.StringVar() # it can be created only after tk.Tk() was used

b = tk.Button(root, text="Hello World!", command=callback)
b.pack()

b = tk.Button(root, text="Exit", command=root.destroy)
b.pack()

root.mainloop()
