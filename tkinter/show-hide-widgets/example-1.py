import tkinter as tk

# --- functions ---

def toggle():
    global buttons
    
    if btn['text'] == 'Show':
        btn['text']  = 'Hide'
        for i, item in enumerate(some_list, 1):
            b = tk.Button(root, text=item)
            b.grid(row=i, column=0, sticky='we')
            buttons.append(b)

    else:
        btn['text'] = 'Show'
        for b in buttons:
            b.destroy() # destroy to free memory
        #buttons.clear() # Python 3 (doesn't need 'global buttons')
        #buttons[:] = [] # Python 2 & 3 (doesn't need 'global buttons')
        buttons = [] # Python 2 & 3 (needs 'global buttons')

        # change 'some_list' to create new buttons
        some_list.append(some_list.pop(0))
        
# --- main ---

root = tk.Tk()

some_list = ['A', 'B', 'C']
buttons = []

btn = tk.Button(root, text='Show', command=toggle)
btn.grid(row=0, column=0, sticky='we')

root.mainloop()
