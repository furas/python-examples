#!/usr/bin/env python3 

# date: 2019.12.07

import tkinter as tk

def update(event):
    widget = event.widget
    idx = widget.curselection()[0]
    val = widget.get(idx)
    print(idx, val)
    lb2.delete(0, "end")
    lb2.insert("end", *options2[val])

options1 = ["A", "B", "C"]
options2 = {
    "A": ["A1", "A2", "A3"],
    "B": ["B1", "B2", "B3"],
    "C": ["C1", "C2", "C3"],
}
root = tk.Tk()

lb1 = tk.Listbox(root)
lb1.pack()
lb1.insert("end", *options1)
lb1.bind('<<ListboxSelect>>', update)

lb2 = tk.Listbox(root)
lb2.pack()
lb2.insert("end", *options2["A"])

root.mainloop()    
