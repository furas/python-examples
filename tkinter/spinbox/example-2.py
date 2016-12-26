import tkinter as tk

# --- functions ---

def callback():
    print("value:", w.get())

# --- main ---

root = tk.Tk()

w = tk.Spinbox(root, state='readonly', from_=1, to=5, command=callback)
w.pack()

root.mainloop()
