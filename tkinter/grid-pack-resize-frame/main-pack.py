
# date: 2019.07.24
# https://stackoverflow.com/questions/57172934/how-to-get-grid-columnconfigure-working-inside-frame-using-grid-manager/57173298#57173298

import tkinter as tk

master = tk.Tk()
master['bg'] = 'red'

f = tk.Frame(master)
f.pack(fill='both', expand=True)

f.grid_columnconfigure(0, weight=1)
f.grid_columnconfigure(2, weight=1)
f.grid_columnconfigure(4, weight=1)

l1 = tk.Label(f, text='Label 1', bg='green')
l2 = tk.Label(f, text='Label 2', bg='green')

l1.grid(row=0, column=1)
l2.grid(row=0, column=3)

master.mainloop()
