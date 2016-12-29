#!/usr/bin/env python3

'''set frame height 10%, 80%, 10%'''
import tkinter as tk

root = tk.Tk()
root.geometry('400x300')

header = tk.Frame(root, bg='green', height=30)
content = tk.Frame(root, bg='red')
footer = tk.Frame(root, bg='green', height=30)

header.pack(fill='both')
content.pack(fill='both')
footer.pack(fill='both', side='bottom')

root.mainloop()
