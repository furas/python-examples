#!/usr/bin/env python3

import tkinter as tk

# --- init ---

root = tk.Tk()
root.title('Grid')

# --- text ---

text = '\n[very, very, very, very, very long text for example]'

# --- info ---

tk.Label(root, text="Bartłomiej 'furas' Burek (blog.furas.pl)", bg='black', fg='white', width=70).grid()
tk.Label(root, text="import tkinter as tk", bg='black', fg='yellow', width=70).grid()

# --- align button/label/widget in cell ---

tk.Label(root, text="\n--------- align button/label/widget in cell ---------", bg='grey', fg='yellow', width=70).grid()
tk.Label(root, text="use in grid(...)\n", bg='grey', fg='white', width=70).grid()

# ---

tk.Button(root, text="\n (nothing) \n"+text).grid()
tk.Button(root, text="\n sticky='w' (or) sticky=tk.W \n"+text).grid(sticky='w')
tk.Button(root, text="\n sticky='e' (or) sticky=tk.E \n"+text).grid(sticky='e')
tk.Button(root, text="\n sticky='we' (or) sticky=tk.W+tk.E \n"+text).grid(sticky='we')

# --- align text in button/label ---

tk.Label(root, text="\n--------- align text in button/label ---------", bg='grey', fg='yellow', width=70).grid()
tk.Label(root, text="use in Label(...)/Button(...)\n", bg='grey', fg='white', width=70).grid()
tk.Label(root, text="grid( sticky='we' (or) sticky=tk.W+tk.E )", bg='gray', width=70).grid()

# ---

tk.Button(root, text="\n (nothing) \n"+text).grid(sticky='we')
tk.Button(root, text="\n anchor='w' (or) anchor=tk.W \n"+text, anchor='w').grid(sticky='we')
tk.Button(root, text="\n anchor='e' (or) anchor=tk.E \n"+text, anchor='e').grid(sticky='we')

# --- align lines in text in button/label ---

tk.Label(root, text="\n--------- align lines in text in button/label ---------", bg='grey', fg='yellow', width=70).grid()
tk.Label(root, text="use in Label(...)/Button(...)\n", bg='grey', fg='white', width=70).grid()
tk.Label(root, text="grid( sticky='we' (or) sticky=tk.W+tk.E )", bg='gray', width=70).grid()

# ---

tk.Button(root, text="\n (nothing)\n"+text).grid(sticky='we')
tk.Button(root, text="\n justify='left' (or) justify=tk.LEFT \n"+text, justify='left').grid(sticky='we')
tk.Button(root, text="\n justify='right' (or) justify=tk.RIGHT \n"+text, justify='right').grid(sticky='we')
tk.Button(root, text="\n justify='center' (or) justify=tk.CENTER \n"+text, justify='center').grid(sticky='we')

# --- info ---

tk.Label(root, text="w = west/left , e = east/right , n = north/top , s = south/bottom", bg='black', fg='white', width=70).grid()

# --- "start the engine" ---

root.mainloop()
