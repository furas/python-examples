# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.26

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tree = ttk.Treeview(root, selectmode="browse")
tree.pack(side='left', fill='both', expand=True)

# `command=tree.yview` sends information from `scrollbar` to `treeview` when `scrollbar` is moved (and threeview is moved too)

scrollbar = tk.Scrollbar(root, orient='vertical', command=tree.yview)
scrollbar.pack(side='right', fill='y')

# `yscrollcommand=scrollbar.set` sends information from `treeview` to `scrollbar` 
# to change size of `scrollbar` when items are added/removed from treeview 
# and to move `scrollbar` when `treeview` is scrolled with mouse wheel.
tree.config(yscrollcommand=scrollbar.set)

for x in range(1, 21):
    print(tree.insert('', 'end', text=str(x)))

root.mainloop()

