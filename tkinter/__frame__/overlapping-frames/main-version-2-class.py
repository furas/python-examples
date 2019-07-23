
# date: 2019.07.22
# https://stackoverflow.com/questions/57137643/multiple-frames-using-tkinker

import tkinter as tk

class MainFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self['bg'] = 'green'
        self['width'] = 800
        self['height'] = 600
        
        self.label = tk.Label(self, text='800x600')
        self.label.place(relx=0.5, rely=0.5, anchor='c')

        self.button1 = tk.Button(self, text="Show")
        self.button1.place(relx=1, rely=1, anchor='se')

        self.button2 = tk.Button(self, text="Show")
        self.button2.place(relx=1, rely=0, anchor='ne')

    def show(self):
        self.place(x=0, y=0, anchor='nw')
        
    #def hide(self):
    #    self.place_forget()


class BottomFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self['bg'] = 'red'
        self['width'] = 800
        self['height'] = 230
        
        self.label = tk.Label(self, text='800x230')
        self.label.place(relx=0.5, rely=0.5, anchor='c')

        self.button = tk.Button(self, text="Hide", command=self.hide)
        self.button.place(relx=1, rely=1, anchor='se')

    def show(self):
        self.place(relx=0, rely=1, anchor='sw')
        
    def hide(self):
        self.place_forget()


class TopFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self['bg'] = 'blue'
        self['width'] = 800
        self['height'] = 230
        
        self.label = tk.Label(self, text='800x230')
        self.label.place(relx=0.5, rely=0.5, anchor='c')

        self.button = tk.Button(self, text="Hide", command=self.hide)
        self.button.place(relx=1, rely=0, anchor='ne')

    def show(self):
        self.place(relx=0, rely=0, anchor='nw')
        
    def hide(self):
        self.place_forget()
    
# --- main ---

root = tk.Tk()
root.geometry('800x600')

f1 = MainFrame()
f1.show()

f2 = BottomFrame()
#f2.show() # hiddem

f3 = TopFrame()
#f3.show() # hiddem

f1.button1['command'] = f2.show
f1.button2['command'] = f3.show

root.mainloop()   
