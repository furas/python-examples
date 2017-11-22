import tkinter as tk

def change_selection(obj):
    global selected

    if selected:
        selected.configure(relief='raised', state='active')
        
    selected = obj
    obj.configure(relief='sunken', state='disabled')

def reset_selection():
    global selected

    selected = None

    x1.configure(relief='raised', state='active')
    x2.configure(relief='raised', state='active')


root = tk.Tk()

selected = None

x1 = tk.Button(root, text="Button 1")
x1.configure(command=lambda:change_selection(x1))
x1.pack(fill='both')

x2 = tk.Button(root, text="Button 2")
x2.configure(command=lambda:change_selection(x2))
x2.pack(fill='both')

b = tk.Button(root, text="Reset", command=reset_selection)
b.pack(fill='both', pady=(10, 0)) # extra space above button

root.mainloop()
