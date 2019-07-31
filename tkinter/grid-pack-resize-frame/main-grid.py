
# date: 2019.07.24
# https://stackoverflow.com/questions/57172934/how-to-get-grid-columnconfigure-working-inside-frame-using-grid-manager/57173298#57173298

import tkinter as tk

master = tk.Tk()
master['bg'] = 'red'

master.grid_rowconfigure(1, weight=1)
master.grid_columnconfigure(1, weight=1)

f = tk.Frame(master, width=400, height=300)
f.grid(row=1, column=1, sticky='news')

f.grid_propagate(False)

f.grid_columnconfigure(0, weight=1)
f.grid_columnconfigure(2, weight=1)
f.grid_columnconfigure(4, weight=1)

l1 = tk.Label(f, text='Label 1', bg='green')
l2 = tk.Label(f, text='Label 2', bg='green')

l1.grid(row=0, column=1)
l2.grid(row=0, column=3)

master.mainloop()
