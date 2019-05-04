
# date: 2019.05.04
# author: Bartłomiej 'furas' Burek

import tkinter as tk

# --- function ---

def main_window():
    global root

    if root is not None:
        root.destroy()

    root = tk.Tk()

    button = tk.Button(root, text="Frame #1", command=window_1)
    button.pack()

    button = tk.Button(root, text="Frame #2", command=window_2)
    button.pack()

    root.mainloop()

def window_1():
    global root

    if root is not None:
        root.destroy()

    root = tk.Tk()

    l = tk.Label(root, text="It is Frame #1", bg='red')
    l.pack()

    b = tk.Button(root, text="BACK", command=main_window)
    b.pack()

    root.mainloop()

def window_2():
    global root

    if root is not None:
        root.destroy()

    root = tk.Tk()

    l = tk.Label(root, text="It is Frame #2", bg='green')
    l.pack()

    b = tk.Button(root, text="BACK", command=main_window)
    b.pack()

    root.mainloop()

# --- main ---

#global value to keep access to open window
root = None

main_window()

