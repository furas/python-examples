import tkinter as tk

#--- functions ---

def on_select(text):
    print('selected text:', text)
    print('---')

#--- main ---
    
data = ['a,b,c', 'x,y,z']
    
root = tk.Tk()

for i, options in enumerate(data):
    options = options.split(',')
    op = tk.OptionMenu(root, tk.StringVar(value=options[0]), *options, command=on_select)
    op.pack()
    
root.mainloop()
