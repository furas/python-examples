#!/usr/bin/env python3

import tkinter as tk

def test():
    # here you can get selected element
    print('previous:', listbox.get('active'))
    print(' current:', listbox.get(listbox.curselection()))

# --- main ---

root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(1, 'Hello 1')
listbox.insert(2, 'Hello 2')
listbox.insert(3, 'Hello 3')
listbox.insert(4, 'Hello 4')
listbox.selection_set(0)

button = tk.Button(root, text="Test", command=test)
button.pack()

root.mainloop()
