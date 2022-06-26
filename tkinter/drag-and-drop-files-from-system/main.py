# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.26

import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

def drop(event):
    text = event.data
    text = text[1:-1]  # remove first and last `{ }`
    for item in text.split('} {'):
        print(item)
        print('---')
        lb.insert('end', item)

# --- main ---

root = TkinterDnD.Tk()

lb = tk.Listbox(root)
lb.pack(fill='both', expand=True)

lb.insert(1, "drag files to here")

# register the listbox as a drop target
lb.drop_target_register(DND_FILES)
lb.dnd_bind('<<Drop>>', drop)

root.mainloop()

