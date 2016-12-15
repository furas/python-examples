import tkinter as tk

# --- functions ---

def on_select(value):
    print('   value:', value)
    print('selected:', selected.get())

# --- main ---
        
root = tk.Tk()

# ---

options = ["one", "two", "three"]

selected = tk.StringVar(value=options[0])

#selected = tk.StringVar()
#selected.set(options[0])

op = tk.OptionMenu(root, selected, *options, command=on_select)
op.pack()

# ---

root.mainloop()
