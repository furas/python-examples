
# date: 2019.10.13
# https://stackoverflow.com/questions/58358089/how-to-create-ui-that-shows-a-hierarchy

import tkinter as tk
from tkinter import ttk

# --- functions ---

def add():
    top = tk.Toplevel()
    tk.Label(top, text="Add").pack()
    name_entry = tk.Entry(top)
    name_entry.pack()

    def on_OK(event=None): # `event` to get argument from `bind <Return>`
        if tree.selection():
            place = tree.selection()[0]
        else:
            place = ''
        item = tree.insert(place, "end", text=name_entry.get())
        tree.item(item, tag=item) # add tag to bind mouse click
        tree.tag_bind(item, '<Double-Button-1>', rename) # rename on double click
        top.destroy()

    name_entry.bind('<Return>', on_OK)
    tk.Button(top, text="OK", command=on_OK).pack(fill='x')
    tk.Button(top, text="Cancel", command=top.destroy).pack(fill='x')
 
def rename(event=None): # `event` to get argument from `bind <Double-Button-1>`
    top = tk.Toplevel()
    tk.Label(top, text="Rename").pack()
    name_entry = tk.Entry(top)
    name_entry.pack()

    def on_OK(event=None): # `event` to get argument from `bind <Return>`
        for item in tree.selection():
            tree.item(item, text=name_entry.get())
        top.destroy()

    name_entry.bind('<Return>', on_OK)
    tk.Button(top, text="OK", command=on_OK).pack(fill='x')
    tk.Button(top, text="Cancel", command=top.destroy).pack(fill='x')
 
def delete():
    top = tk.Toplevel()
    tk.Label(top, text="Delete").pack()
    tk.Label(top, text="Are you sure?").pack()
    
    def on_OK(event=None): # `event` to get argument from `bind <Return>`
        for item in tree.selection():
            tree.delete(item)
        top.destroy()
 
    tk.Button(top, text="OK", command=on_OK).pack(fill='x')
    tk.Button(top, text="Cancel", command=top.destroy).pack(fill='x')
 
# --- main ---

my_app = tk.Tk()

tk.Button(my_app,text="add", command=add).pack(fill='x')
tk.Button(my_app,text="delete", command=delete).pack(fill='x')
tk.Button(my_app,text="rename", command=rename).pack(fill='x')
  
tree = ttk.Treeview(my_app)
tree.column("#0", width=270, minwidth=270)
tree.pack(side='top', fill='x')
 
my_app.mainloop()
