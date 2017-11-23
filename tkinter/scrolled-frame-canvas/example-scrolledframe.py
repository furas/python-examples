import tkinter as tk
from scrolledframe import ScrolledFrame

# --- functions ---

def test_checkbuttons():
    for index, var in enumerate(variables):
        if var.get() > 0:
            print('index:', index, 'data:', data[index])
            
# --- main ---

root = tk.Tk()              

# ---

# create scrolled frame
sf = ScrolledFrame(root)
sf.pack(fill='both', expand=True) # resize with window

# internal config
#sf._canvas['background'] = 'red'
#sf.frame['background'] = 'green'
#sf.frame['padx'] = 10

# ---

# add to scrolled frame

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
variables = []

# add widgets to scrolled frame - as parent you have to use `sf.frame` instead of `sf`
for txt in data:
    var = tk.IntVar()
    variables.append(var)
    l = tk.Checkbutton(sf.frame, text=txt, variable=var)
    l.grid(sticky='w')

# ---

b = tk.Button(root, text='Test checkbuttons', command=test_checkbuttons)
b.pack()

# ---

root.mainloop()


