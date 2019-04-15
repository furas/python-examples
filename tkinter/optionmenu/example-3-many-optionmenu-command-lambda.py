import tkinter as tk

#--- functions ---

def on_select(text, number):
    print('selected text:', text)
    print('OptionMenu\'s number:', number)
    print('data[number]:', data[number])
    print('---')

#--- main ---
    
data = ['a,b,c', 'x,y,z']
    
root = tk.Tk()

for i, options in enumerate(data):
    options = options.split(',')
    op = tk.OptionMenu(root, tk.StringVar(value=options[0]), *options, command=lambda text, number=i:on_select(text, number))
    op.pack()
    
root.mainloop()
