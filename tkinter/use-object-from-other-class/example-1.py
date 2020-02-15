import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry = tk.Entry(self)
        self.entry.pack()

class Keyboard(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
    
        buttons = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9'],
        ]
        
        for y, row in enumerate(buttons):    
            for x, item in enumerate(row):
                b = tk.Button(self, text=item, command=lambda value=item:self.append(value))
                b.grid(row=y, column=x)
    
    def append(self, text):
        self.parent.entry.insert('end', text)
        
app = Main()
ctr = Keyboard(app)
app.mainloop()


