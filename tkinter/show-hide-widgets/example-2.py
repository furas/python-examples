import tkinter as tk

# --- functions ---

def toggle():
    
    if btn['text'] == 'Show':
        btn['text']  = 'Hide'
        for i, b in enumerate(buttons, 1):
            b.grid(row=i, column=0, sticky='we')

    else:
        btn['text'] = 'Show'
        for b in buttons:
            b.grid_forget()

# --- main ---

root = tk.Tk()

some_list = ['A', 'B', 'C']
buttons = []
for i, item in enumerate(some_list):
    b = tk.Button(root, text=item)
    buttons.append(b)

btn = tk.Button(root, text='Show', command=toggle)
btn.grid(row=0, column=0, sticky='we')

root.mainloop()
