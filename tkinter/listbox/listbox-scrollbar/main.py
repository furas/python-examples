# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.11

import tkinter as tk

root = tk.Tk()

# - create -

listbox = tk.Listbox(root)
listbox.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(root, orient='vertical', command=listbox.yview)
scrollbar.pack(side='right', fill='y')
#scrollbar.pack(side='left', fill='y')  # `left` also works

listbox.config(yscrollcommand=scrollbar.set)

# - add some values to listbox for scrolling -

for i in range(50):
    listbox.insert('end', str(i))

# - start -

root.mainloop()

