#!/usr/bin/env python3

# date: 2020.01.06
# https://stackoverflow.com/questions/59604932/tkinter-how-to-go-to-the-top-of-a-treeview-when-pressing-down-at-the-bottom-a

import tkinter as tk
from tkinter import ttk

def jump_to_first(event):
    last = tree.get_children()[-1]
    if tree.focus() == last:
        first = tree.get_children()[0]
        tree.selection_set(first) # move selection
        tree.focus(first) # move focus
        tree.see(first) # scroll to show it
        return "break" # don't send event to TreeView

def jump_to_last(event):
    first = tree.get_children()[0]
    if tree.focus() == first:
        last = tree.get_children()[-1]
        tree.selection_set(last) # move selection
        tree.focus(last) # move focus
        tree.see(last) # scroll to show it
        return "break" # don't send event to TreeView

root = tk.Tk()

tree = ttk.Treeview(root, selectmode="browse")
tree.pack()

for x in range(1, 21):
    print(tree.insert('', 'end', text=str(x)))

tree.bind('<Down>', jump_to_first)
tree.bind('<Up>', jump_to_last)

root.mainloop()

