import tkinter as tk

# --- functions ---

def on_change_selection(value):
    print('   value:', value, '--->', data[value])
    print('selected:', selected.get(), '--->', data[value])

# --- main ---
        
root = tk.Tk()

# ---

data = {
    "one": "Hello first World",
    "two": "Hello second World ",
    "three": "Hello third World",
}    

options = sorted(data)

selected = tk.StringVar(value=options[0])

#selected = tk.StringVar()
#selected.set(options[0])

op = tk.OptionMenu(root, selected, *options, command=on_change_selection)
op.pack()

# ---

root.mainloop()
