
# date: 2019.10.13
# https://stackoverflow.com/questions/58358089/how-to-create-ui-that-shows-a-hierarchy

import tkinter as tk
from tkinter import ttk

# --- functions ---
 
def rename(event=None): # `event` to get argument from double click
    top = tk.Toplevel()
    name_entry = tk.Entry(top)
    name_entry.pack()

    def on_enter(event):
        selected = tree.selection()[0]
        print(selected)
        print(tree.item(selected)['text'], name_entry.get())
        #tree.item(selected)['text'] = name_entry.get()
        tree.item(selected, text=name_entry.get())
        print(tree.item(selected)['text'], name_entry.get())
        top.destroy()

    name_entry.bind('<Return>', on_enter)
 
def add():
    top = tk.Toplevel()
    tk.Label(top, text="Name").pack()
    name_entry = tk.Entry(top)
    name_entry.pack()

    def on_OK():
        item = tree.insert(tree.selection(), "end", text=name_entry.get())
        tree.item(item, tag=item) # add tag to bind mouse click
        tree.tag_bind(item, '<Double-Button-1>', rename) # rename on double click
        top.destroy()

    tk.Button(top, text="OK", command=on_OK).pack(fill='x')
    tk.Button(top, text="Cancel", command=quit).pack(fill='x')
 
def delete():
    if tree.selection():
        tree.delete(tree.selection())
 
# --- main ---

my_app = tk.Tk()

tk.Button(my_app,text="add", command=add).pack(fill='x')
tk.Button(my_app,text="delete", command=delete).pack(fill='x')
tk.Button(my_app,text="rename", command=rename).pack(fill='x')
  
tree = ttk.Treeview(my_app)
tree.column("#0", width=270, minwidth=270)
tree.pack(side='top', fill='x')
 
my_app.mainloop()
