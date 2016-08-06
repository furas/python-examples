import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

s = ttk.Style()

#s.configure('TButton', background='green')

bg = s.lookup('TButton', 'background')

s.map('TButton',
#    background=[('active', 'red')]
    background=[('active', bg)]
)

btn1 = ttk.Button(root, text='Sample', style='TButton')
btn1.pack()

btn2 = ttk.Button(root, text='Sample')
btn2.pack()

root.mainloop()
