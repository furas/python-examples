# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.03.11

import tkinter as tk

class ScrolledListbox(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.listbox = tk.Listbox(self)
        self.listbox.pack(side='left', fill='both', expand=True)

        self.scrollbar = tk.Scrollbar(self, orient='vertical', command=self.listbox.yview)
        self.scrollbar.pack(side='right', fill='y')
        #self.scrollbar.pack(side='left', fill='y')  # `left` also works

        self.listbox.config(yscrollcommand=self.scrollbar.set)

# - main -

root = tk.Tk()

# - create -

lb1 = ScrolledListbox(root)
lb1.pack(side='left', fill='both', expand=True)

lb2 = ScrolledListbox(root)
lb2.pack(side='left', fill='both', expand=True)

lb3 = ScrolledListbox(root)
lb3.pack(side='left', fill='both', expand=True)

# - add some values to listbox for scrolling -

for i in range(50):
    lb1.listbox.insert('end', str(i))
    lb2.listbox.insert('end', str(i+100))
    lb3.listbox.insert('end', str(i+200))

# - start -

root.mainloop()

