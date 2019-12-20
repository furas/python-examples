#!/usr/bin/env python3 

# date: 2019.12.11

import tkinter as tk

WIDTH = 800
HEIGHT = 600
root = tk.Tk()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width-WIDTH)//2
y = (screen_height-HEIGHT)//2
root.geometry('{}x{}+{}+{}'.format(WIDTH, HEIGHT, x, y))

root.overrideredirect(True) # borderless window, can't be close and it is always on top
#root.update_idletasks()    # DON'T need it but if it is needed then can't be before `overrideredirect()`

button = tk.Button(root, text='QUIT', command=root.destroy)
button.place(relx=.5, rely=0.5, anchor='center')

root.mainloop()

