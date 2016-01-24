#!/usr/bin/env python3

import tkinter as tk

# --- init ---

root = tk.Tk()
root.title('Pack')

# --- text ---

text = '\n[very, very, very, very, very long text for example]'

# --- info ---

tk.Label(root, text="Bartłomiej 'furas' Burek (blog.furas.pl)", bg='black', fg='white', width=70).pack()
tk.Label(root, text="import tkinter as tk", bg='black', fg='yellow', width=70).pack()

# --- align button/label/widget in cell ---

tk.Label(root, text="\n--------- align button/label/widget in cell ---------", bg='grey', fg='yellow', width=70).pack()
tk.Label(root, text="use in pack(...)\n", bg='grey', fg='white', width=70).pack()

# ---

tk.Button(root, text="\n (nothing) \n"+text).pack()
tk.Button(root, text="\n anchor='w' (or) anchor=tk.W \n"+text).pack(anchor='w')
tk.Button(root, text="\n anchor='e' (or) anchor=tk.E \n"+text).pack(anchor='e')
#tk.Label(root, text="\nCAN'T DO: anchor='we' (or) anchor=tk.W+tk.E\n", fg='red').pack()
tk.Button(root, text="\n fill='x' (or) fill=tk.X \n"+text).pack(fill='x')

# --- align text in button/label ---
 
tk.Label(root, text="\n--------- align text in button/label ---------", bg='grey', fg='yellow', width=70).pack()
tk.Label(root, text="use in Label(...)/Button(...)\n", bg='grey', fg='white', width=70).pack()
tk.Label(root, text="pack( fill='x' (or) fill=tk.X )", bg='gray', width=70).pack()

# ---

tk.Button(root, text="\n (nothing) \n"+text).pack(fill='x')
tk.Button(root, text="\n anchor='w' (or) anchor=tk.W \n"+text, anchor='w').pack(fill='x')
tk.Button(root, text="\n anchor='e' (or) anchor=tk.E \n"+text, anchor='e').pack(fill='x')

# --- align lines in text in button/label ---
 
tk.Label(root, text="\n--------- align lines in text in button/label ---------", bg='grey', fg='yellow', width=70).pack()
tk.Label(root, text="use in Label(...)/Button(...)\n", bg='grey', fg='white', width=70).pack()
tk.Label(root, text="pack( fill='x' (or) fill=tk.X )", bg='gray', width=70).pack()

# ---

tk.Button(root, text="\n (nothing) \n"+text).pack(fill='x')
tk.Button(root, text="\n justify='left' (or) justify=tk.LEFT \n"+text, justify='left').pack(fill='x')
tk.Button(root, text="\n justify='right' (or) justify=tk.RIGHT \n"+text, justify='right').pack(fill='x')
tk.Button(root, text="\n justify='center' (or) justify=tk.CENTER \n"+text, justify='center').pack(fill='x')

# --- info --- 

tk.Label(root, text="w = west/left , e = east/right , n = north/top , s = south/bottom", bg='black', fg='white', width=70).pack()

# --- "start the engine" ---

root.mainloop()
