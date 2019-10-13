#!/usr/bin/env python3

# date: 2019.10.12

import tkinter as tk

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.shared_data ={
            "email": tk.StringVar(),
            "password": tk.StringVar()
        }
        
        self.frames = {
            'StartPage': StartPage(self, self),
            'PageTwo': PageTwo(self, self),
        }
        
        self.current_frame = None
        self.show_frame('StartPage')

    def show_frame(self, name):
        if self.current_frame:
            self.current_frame.forget()
        self.current_frame = self.frames[name]
        self.current_frame.update_widgets()
        self.current_frame.pack()
                            
class BasePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        pass
    
    def update_widgets(self):
        pass
                            
class StartPage(BasePage):

    def create_widgets(self):
        self.entry1 = tk.Entry(self, textvariable=self.controller.shared_data["email"])
        self.entry1.pack()
        self.entry2 = tk.Entry(self, show='*')
        self.entry2.pack()
        button = tk.Button(self, text="Submit", command=lambda:self.controller.show_frame("PageTwo"))
        button.pack()
    
class PageTwo(BasePage):

    def create_widgets(self):
        self.label = tk.Label(self, text="")
        self.label.pack()

        button = tk.Button(self, text="Back", command=lambda:self.controller.show_frame("StartPage"))
        button.pack()

    def update_widgets(self):
        self.label["text"] = "Welcome, {}".format(self.controller.shared_data["email"].get())
        
        
if __name__ == "__main__":
    win = Main()
    win.mainloop()
