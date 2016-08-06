#!/usr/bin/env python3

'''button hover color'''

import tkinter as tk


root = tk.Tk()

# default hover color
button0 = tk.Button(root, text='Default hover color')
button0.pack()

# own hover color
button1 = tk.Button(root, text='Own hover color', activebackground='red')
button1.pack()

# none hover color
button2 = tk.Button(root, text='None hover color')

system_bg = button2.cget('background')
button2.config(activebackground=system_bg)

button2.pack()

# activebackground='SystemButtonFace' doesn't work on Linux

root.mainloop()
