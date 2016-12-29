import tkinter as tk

# --- functions ---

def toggle():
    
    if btn['text'] == 'Show':
        btn['text']  = 'Hide'
        frame.grid(row=16, column=0, sticky='we')
    else:
        btn['text'] = 'Show'
        frame.grid_forget()

# --- main ---

root = tk.Tk()

some_list = ['A', 'B', 'C']

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1) # resise column

for i, item in enumerate(some_list):
    b = tk.Button(frame, text=item)
    b.grid(row=i, column=0, sticky='we')

btn = tk.Button(root, text='Show', command=toggle)
btn.grid(row=0, column=0, sticky='we')

root.mainloop()
