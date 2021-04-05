import tkinter as tk
from scrolledcanvas import ScrolledCanvas

# --- functions ---

def test_checkbuttons():
    print('--- test_checkbuttons ---')
    
    for index, var in enumerate(variables):
        if var.get() > 0:
            print('index:', index, 'data:', data[index])
            
# --- main ---

root = tk.Tk()              

# create scroller
s = ScrolledCanvas(root)
s.pack(fill='both', expand=True)

# ---

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
variables = []

f = tk.Frame(s)

# add widgets to frame - as parent you uses `f`
for txt in data:
    var = tk.IntVar()
    variables.append(var)
    l = tk.Checkbutton(f, text=txt, variable=var)
    l.grid(sticky="w")

# add frame to scrolledcanvas - as parent you uses `f`
print('f:', f.master)
s.add(f)
print('f:', f.master)

# ---

b = tk.Button(root, text='Test checkbuttons', command=test_checkbuttons)
b.pack()

# ---

root.mainloop()

