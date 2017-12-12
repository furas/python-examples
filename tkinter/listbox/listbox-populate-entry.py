import tkinter as tk

# --- function ---

def on_selection(event):
    line = event.widget.get(event.widget.curselection())

    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    
    e1.insert('end', line[:10].strip())
    e2.insert('end', line[11:26].strip())
    e3.insert('end', line[27:].strip())
    
# --- main ---

root = tk.Tk()
root.geometry('400x300')

listbox = tk.Listbox(root, font=('monospace', 10), selectbackground='red')
listbox.pack(expand='yes', fill='both')

listbox.insert('end', '{:10s}|{:15s}|{:10s}'.format('123', 'Bob',   'Active'))
listbox.insert('end', '{:10s}|{:15s}|{:10s}'.format('212', 'Jim',   'Off'))
listbox.insert('end', '{:10s}|{:15s}|{:10s}'.format('417', 'Johny', 'Off'))

listbox.bind('<<ListboxSelect>>', on_selection)

e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

e3 = tk.Entry(root)
e3.pack()

root.mainloop()
