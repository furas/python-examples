#!/usr/bin/env python3

'''
ttk.Button hover color

http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Button.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-style-layer.html
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-map.html

http://www.tkdocs.com/tutorial/styles.html
'''

import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

s = ttk.Style()

# --- default hover color ---

button0 = ttk.Button(root, text='Default hover color')
button0.pack()

# --- own hover color ---

s.map('Button1.TButton', background=[('active', 'red')] )

button1 = ttk.Button(root, text='Own hover color', style='Button1.TButton')
button1.pack()

# --- none hover color ---

system_bg = s.lookup('TButton', 'background')
s.map('Button2.TButton', background=[('active', system_bg)])

button2 = ttk.Button(root, text='None hover color', style='Button2.TButton')
button2.pack()

# ---

root.mainloop()
