
# date: 2019.04.07
# bug with raising canvas - solution: tk.Misc.tkraise(self)
# https://stackoverflow.com/a/55559387/1832058

import tkinter as tk


class MyCustomButton(tk.Canvas):
    
    def __init__(self, master):
        super().__init__(master, width=50, height=50, background='blue')
        
    def lift(self):
        tk.Misc.tkraise(self)


class Example(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.canvas = tk.Canvas(self, width=200, height=200)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.button3 = tk.Button(self.canvas, text="button3")
        self.custom_button1 = MyCustomButton(self.canvas)
        self.custom_button2 = MyCustomButton(self.canvas)
        
        self.canvas.create_window(20, 20, anchor='nw', window=self.button3)
        self.canvas.create_window(50, 40, anchor='nw', window=self.custom_button1)
        self.canvas.create_window(10, 40, anchor='nw', window=self.custom_button2)

        self.button3.bind("<Button-1>", self.click_handler)
        self.custom_button1.bind("<Button-1>", self.click_handler)
        self.custom_button2.bind("<Button-1>", self.click_handler)


    def click_handler(self,event):
        event.widget.lift() #raises exception if event.widget is a MyCustomButton
            
if __name__ == "__main__":
    root = tk.Tk()
    ex = Example(root)
    ex.pack(fill="both", expand=True)
    root.mainloop()
