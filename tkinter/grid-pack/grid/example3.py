import tkinter as tk

root = tk.Tk()
root.geometry('300x300')

root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

l_1_1 = tk.Label(root, text='text', bg='red')
l_1_1.grid(row=1, column=1)
l_1_2 = tk.Label(root, text='text', bg='red')
l_1_2.grid(row=1, column=2)
l_1_3 = tk.Label(root, text='text', bg='red')
l_1_3.grid(row=1, column=3)

l_2 = tk.Label(root, text='very very long text', bg='green')
l_2.grid(row=2, column=1, columnspan=3)

root.mainloop()
