import tkinter as tk    

class CalcKeyboard(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        
        ls = (
            ("7", "8", "9", "/"),
            ("4", "5", "6", "x"),
            ("1", "2", "3", "-"),
            ("0", ".", "%", "+"),
            ("="),
        )

        self.result = tk.Entry(self)
        self.result.grid(row=0, column=0, sticky='news', columnspan=4)

        for r, row in enumerate(ls, 1):
            for c, item in enumerate(row):
                bt = tk.Button(self, text=item, command=lambda char=item:self.on_press(char))
                if len(row) > 1:
                    bt.grid(row=r, column=c, sticky='news')
                else:
                    print('')
                    bt.grid(row=r, column=c, sticky='news', columnspan=4)

    def on_press(self, char):
        print(char)
        
class Calc():

    def __init__(self, master):
        
        keyboard1 = CalcKeyboard(master)
        keyboard1.grid(row=0, column=0)

        keyboard2 = CalcKeyboard(master)
        keyboard2.grid(row=0, column=1)
        
        keyboard3 = CalcKeyboard(master)
        keyboard3.grid(row=1, column=0)

        keyboard4 = CalcKeyboard(master)
        keyboard4.grid(row=1, column=1)
        
# --- main ---

root = tk.Tk()
cal = Calc(root)
root.mainloop()
