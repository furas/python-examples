import tkinter as tk
import random

def move():
    f.place_forget()
    new_x = random.randint(0, 100)
    new_y = random.randint(0, 150)
    f.place(x=new_x, y=new_y)

root = tk.Tk()

f = tk.Frame(root)
f.place(x=0, y=0)

tk.Label(f, text='HELLO!').pack()
tk.Button(f, text='Move it', command=move).pack()

root.mainloop()
