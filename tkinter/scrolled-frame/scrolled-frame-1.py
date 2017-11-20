import tkinter as tk

# --- classes ---

class ScrolledFrame(tk.Frame):

    def __init__(self, parent, vertical=True, horizontal=False):
        super().__init__(parent)
        
        self._canvas = tk.Canvas(self)
        self._canvas.grid(row=0, column=0)

        self._vertical_bar = tk.Scrollbar(self, orient="vertical", command=self._canvas.yview)
        if vertical:
            self._vertical_bar.grid(row=0, column=1, sticky="ns")
        self._canvas.configure(yscrollcommand=self._vertical_bar.set)

        self._horizontal_bar = tk.Scrollbar(self, orient="horizontal", command=self._canvas.xview)
        if horizontal:
            self._horizontal_bar.grid(row=1, column=0, sticky="we")
        self._canvas.configure(xscrollcommand=self._horizontal_bar.set)

        self.inner = tk.Frame(self._canvas)
        self._canvas.create_window((0, 0), window=self.inner, anchor="nw")

        self.inner.bind("<Configure>", self.resize)

    def resize(self, event=None): 
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))

# --- functions ---

def test_checkbuttons():
    for index, var in enumerate(variables):
        if var.get() > 0:
            print('index:', index, 'data:', data[index])
            
# --- main ---

root = tk.Tk()              

# create scrolled frame
sf = ScrolledFrame(root)
#sf._canvas['background'] = 'red'
sf.pack()

# ---

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
variables = []

# add widgets to scrolled frame - as parent you have to use `sf.inner` instead of `sf`
for txt in data:
    var = tk.IntVar()
    variables.append(var)
    l = tk.Checkbutton(sf.inner, text=txt, variable=var)
    l.grid(sticky="w")

# ---

b = tk.Button(root, text='Test checkbuttons', command=test_checkbuttons)
b.pack()

# ---

root.mainloop()


