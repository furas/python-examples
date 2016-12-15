import tkinter as tk

# --- functions ---

def on_change_selection(value):
    print('   value:', value)
    print('selected:', selected.get())

# --- main ---
        
root = tk.Tk()

# ---

options = ["one", "two", "three"]

selected = tk.StringVar(value=options[0])

#selected = tk.StringVar()
#selected.set(options[0])

op = tk.OptionMenu(root, selected, *options, command=on_change_selection)
op.pack()

# ---

root.mainloop()
