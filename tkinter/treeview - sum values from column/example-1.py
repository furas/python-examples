import tkinter as tk
from tkinter import ttk

# --- functions ---

def add_item(a, b, c):
    global global_total

    global_total += c

    tree.insert('', 0, values=(a, b, c))

def calculate_sum():

    total = 0.0

    for child in tree.get_children():
        total += float(tree.item(child, 'values')[2])

    print('Total:', total)

    result['text'] = 'Total: {:.2f}'.format(total)

# --- main ---

global_total = 0.0

# - GUI -

root = tk.Tk()
tree = ttk.Treeview(root, height=4, show="headings", columns=('col1','col2','col3'))
tree.pack()

tree.heading('col1', text='Number')
tree.heading('col2', text='Name')
tree.heading('col3', text='Price')

add = tk.Button(root, text='Sum', command=calculate_sum)
add.pack()

result = tk.Label(root, text='Total: 0')
result.pack()

add_item("1", "AAA", 1.11)
add_item("2", "BBB", 2.22)
add_item("3", "CCC", 3.33)

root.mainloop()

print('Total:', global_total)
