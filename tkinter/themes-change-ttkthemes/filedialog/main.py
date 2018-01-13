import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import ttkthemes

def open_dialog(name):
    root.style.theme_use(name)
    filedialog.askdirectory()

root = tk.Tk()

root.style = ttkthemes.ThemedStyle()
print(root.style.theme_names())

for i, name in enumerate(sorted(root.style.theme_names())):
    b = ttk.Button(root, text=name, command=lambda var=name:open_dialog(var))
    b.pack(fill='x')
    
root.mainloop()
