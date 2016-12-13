#!/usr/bin/env python3

import tkinter as tk

# --- init ---

root = tk.Tk()
root.title('Pack')

# --- text ---

text = '\n[very, very, very, very, very long text for example]'


# --- info ---

f00 = tk.Frame(root)
f00.grid(row=0, column=0, columnspan=2)

tk.Label(f00, text="Bartłomiej 'furas' Burek (blog.furas.pl)", bg='black', fg='white', width=140).grid()
tk.Label(f00, text="import tkinter as tk", bg='black', fg='yellow', width=140).grid()



# --- align button/label/widget in cell ---

f10 = tk.Frame(root)
f10.grid(row=1, column=0, stick='n')

tk.Label(f10, text="\n--------- align button/label/widget in cell ---------", bg='grey', fg='yellow', width=70).grid()
tk.Label(f10, text="use in grid(...)\n", bg='grey', fg='white', width=70).grid()

# ---

tk.Button(f10, text="\n (nothing) \n"+text).grid()
tk.Button(f10, text="\n sticky='w' (or) sticky=tk.W \n"+text).grid(sticky='w')
tk.Button(f10, text="\n sticky='e' (or) sticky=tk.E \n"+text).grid(sticky='e')
tk.Button(f10, text="\n sticky='we' (or) sticky=tk.W+tk.E \n"+text).grid(sticky='we')



# --- align button/label/widget in cell ---

f11 = tk.Frame(root)
f11.grid(row=1, column=1, stick='n')

tk.Label(f11, text="\n--------- align button/label/widget in cell ---------", bg='grey', fg='yellow', width=70).pack()
tk.Label(f11, text="use in pack(...)\n", bg='grey', fg='white', width=70).pack()

# ---

tk.Button(f11, text="\n (nothing) \n"+text).pack()
tk.Button(f11, text="\n anchor='w' (or) anchor=tk.W \n"+text).pack(anchor='w')
tk.Button(f11, text="\n anchor='e' (or) anchor=tk.E \n"+text).pack(anchor='e')
#tk.Label(f11, text="\nCAN'T DO: anchor='we' (or) anchor=tk.W+tk.E\n", fg='red').pack()
tk.Button(f11, text="\n fill='x' (or) fill=tk.X \n"+text).pack(fill='x')




# --- align text in button/label ---

f20 = tk.Frame(root)
f20.grid(row=2, column=0, stick='n')

 
tk.Label(f20, text="\n--------- align text in button/label ---------", bg='grey', fg='yellow', width=70).pack()
tk.Label(f20, text="use in Label(...)/Button(...)\n", bg='grey', fg='white', width=70).pack()
tk.Label(f20, text="pack( fill='x' (or) fill=tk.X )", bg='gray', width=70).pack()

# ---

tk.Button(f20, text="\n (nothing) \n"+text).pack(fill='x')
tk.Button(f20, text="\n anchor='w' (or) anchor=tk.W \n"+text, anchor='w').pack(fill='x')
tk.Button(f20, text="\n anchor='e' (or) anchor=tk.E \n"+text, anchor='e').pack(fill='x')



# --- align lines in text in button/label ---

f21 = tk.Frame(root)
f21.grid(row=2, column=1, stick='n')

tk.Label(f21, text="\n--------- align lines in text in button/label ---------", bg='grey', fg='yellow', width=70).pack()
tk.Label(f21, text="use in Label(...)/Button(...)\n", bg='grey', fg='white', width=70).pack()
tk.Label(f21, text="pack( fill='x' (or) fill=tk.X )", bg='gray', width=70).pack()

# ---

tk.Button(f21, text="\n (nothing) \n"+text).pack(fill='x')
tk.Button(f21, text="\n justify='left' (or) justify=tk.LEFT \n"+text, justify='left').pack(fill='x')
tk.Button(f21, text="\n justify='right' (or) justify=tk.RIGHT \n"+text, justify='right').pack(fill='x')
tk.Button(f21, text="\n justify='center' (or) justify=tk.CENTER \n"+text, justify='center').pack(fill='x')



# --- info ---

tk.Label(root, text="w = west/left , e = east/right , n = north/top , s = south/bottom", bg='black', fg='white', width=140).grid(columnspan=2)

# --- "start the engine" ---

root.mainloop()
