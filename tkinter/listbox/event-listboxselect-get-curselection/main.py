#!/usr/bin/env python3

import tkinter as tk

# --- function ---

def on_selection(event):
    # here you can get selected element
    print('previous:', listbox.get('active'))
    print(' current:', listbox.get(listbox.curselection()))
    
    # or using `event`
    
    #print('event:', event)
    #print('widget:', event.widget)
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    
    print('---')
    
# --- main ---

root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(1, 'Hello 1')
listbox.insert(2, 'Hello 2')
listbox.insert(3, 'Hello 3')
listbox.insert(4, 'Hello 4')

listbox.bind('<<ListboxSelect>>', on_selection)

root.mainloop()
