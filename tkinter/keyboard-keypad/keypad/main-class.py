
# date: 2019.07.23
# https://stackoverflow.com/questions/57161644/how-to-pop-up-an-on-screen-keyboard-to-enter-some-data-in-an-entry-gadget-in-tki/57162755?noredirect=1#comment100841209_57162755

import tkinter as tk

# --- classes ---

class Keypad(tk.Frame):

    buttons = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['0', '.', '-'],
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.target = None
        self.memory = ''
        
        self.create_ui()
        
    def create_ui(self):
        for y, row in enumerate(self.buttons):
            for x, item in enumerate(row):            
                b = tk.Button(self, text=item, command=lambda text=item:self.append(text))
                b.grid(row=y, column=x, sticky='news')

        x = tk.Button(self, text='Backspace', command=self.backspace)
        x.grid(row=0, column=10, sticky='news')

        x = tk.Button(self, text='Clear', command=self.clear)
        x.grid(row=1, column=10, sticky='news')

        x = tk.Button(self, text='Copy', command=self.copy)
        x.grid(row=9, column=0, sticky='news', columnspan='3')

        x = tk.Button(self, text='Paste', command=self.paste)
        x.grid(row=9, column=10, sticky='news')

        self.label = tk.Label(self, text='memory:')
        self.label.grid(row=8, column=0, columnspan=11, sticky='news')

        x = tk.Button(self, text='Hide', command=self.hide)
        x.grid(row=10, column=0, columnspan=11, sticky='news')

    def get(self):
        if self.target:
            return self.target.get()
    
    def append(self, text):
        if self.target:
            self.target.insert('end', text)
    
    def clear(self):
        if self.target:
            self.target.delete(0, 'end')

    def backspace(self):
        if self.target:
            text = self.get()
            text = text[:-1]
            self.clear()
            self.append(text)

    def copy(self):
        #TODO: copy to clipboad
        if self.target:
            self.memory = self.get()
            self.label['text'] = 'memory: ' + self.memory
            print(self.memory)
        
    def paste(self):
        #TODO: copy from clipboad
        if self.target:
            self.append(self.memory)

    def show(self, entry):
        self.target = entry
    
        self.place(relx=0.5, rely=0.5, anchor='c')
    
    def hide(self):
        self.target = None

        self.place_forget()

# --- main ---

root = tk.Tk()
root.geometry('600x400')

keypad = Keypad(root, borderwidth=1, relief='sunken') # sunken, raised, groove, ridge

f = tk.Frame(root)
f.pack()

e1 = tk.Entry(f)
e1.grid(row=0, column=0, sticky='news')
b1 = tk.Button(f, text='Keypad', command=lambda:keypad.show(e1))
b1.grid(row=0, column=1, sticky='news')

e2 = tk.Entry(f)
e2.grid(row=1, column=0, sticky='news')
b2 = tk.Button(f, text='Keypad', command=lambda:keypad.show(e2))
b2.grid(row=1, column=1, sticky='news')

root.mainloop()

