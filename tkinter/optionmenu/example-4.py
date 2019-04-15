import tkinter as tk

#--- functions ---

def on_click():
	for number, var in enumerate(all_variables):
		print('optionmenu:', number, '| selected:', var.get(), '| all:', data[number])

#--- main ---

data = ['a,b,c', 'x,y,z']

root = tk.Tk()

all_variables = []

for options in data:
    options = options.split(',')
    var = tk.StringVar(value=options[0])
    all_variables.append(var)
    op = tk.OptionMenu(root, var, *options)
    op.pack()

b = tk.Button(root, text='OK', command=on_click)
b.pack()

root.mainloop()
