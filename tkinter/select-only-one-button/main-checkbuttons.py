import tkinter as tk

def change_selection(obj):
    global selected

    if selected:
        selected.deselect()
        
    selected = obj

def reset_selection():
    global selected

    selected = None

    x1.deselect()
    x2.deselect()


root = tk.Tk()

selected = None

x1 = tk.Checkbutton(root, text="Checkbutton 1")
x1.configure(command=lambda:change_selection(x1))
x1.pack(fill='both')

x2 = tk.Checkbutton(root, text="Checkbutton 2")
x2.configure(command=lambda:change_selection(x2))
x2.pack(fill='both')

b = tk.Button(root, text="Reset", command=reset_selection)
b.pack(fill='both', pady=(10, 0)) # extra space above button

root.mainloop()
