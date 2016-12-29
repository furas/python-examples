#!/usr/bin/env python3

'''set frame height 10%, 80%, 10%'''
import tkinter as tk

root = tk.Tk()
root.geometry('400x300')

header = tk.Frame(root, bg='green')
content = tk.Frame(root, bg='red')
footer = tk.Frame(root, bg='green')

root.columnconfigure(0, weight=1) # 100%

root.rowconfigure(0, weight=1) # 10%
root.rowconfigure(1, weight=8) # 80%
root.rowconfigure(2, weight=1) # 10%

header.grid(row=0, sticky='news')
content.grid(row=1, sticky='news')
footer.grid(row=2, sticky='news')

root.mainloop()
