#!/usr/bin/env python3

# date: 2019.10.15
# https://stackoverflow.com/questions/58364159/printing-text-from-a-function-into-a-tkinter-label

import os
import tkinter as tk

def get_filenames():
    filenames = sorted(os.listdir('.'))
    text = "\n".join(filenames)
    label['text'] = text # change text in label


root = tk.Tk()

label = tk.Label(root) # empty label 
label.pack()

tk.Button(root, text="OK", command=get_filenames).pack()

root.mainloop()
