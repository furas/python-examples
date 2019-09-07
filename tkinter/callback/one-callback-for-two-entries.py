
# date: 2019.08.23
# 

import tkinter as tk

def return_entry(event):
    content = event.widget.get()
    print(content)

root = tk.Tk()

entry1 = tk.Entry(root)
entry1.pack()

entry1.bind('<Return>', return_entry)

entry2 = tk.Entry(root)
entry2.pack()

entry2.bind('<Return>', return_entry)

root.mainloop()


