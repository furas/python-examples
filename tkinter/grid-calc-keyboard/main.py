import tkinter as tk    

class Calc:

    def __init__(self, master):
        ls = (
            ("7", "8", "9", "/"),
            ("4", "5", "6", "x"),
            ("1", "2", "3", "-"),
            ("0", ".", "%", "+"),
            ("="),
        )

        self.result = tk.Entry(master)
        self.result.grid(row=0, column=0, sticky='news', columnspan=4)

        for r, row in enumerate(ls, 1):
            for c, item in enumerate(row):
                bt = tk.Button(master, text=item, command=lambda char=item:self.on_press(char))
                if len(row) > 1:
                    bt.grid(row=r, column=c, sticky='news')
                else:
                    print('')
                    bt.grid(row=r, column=c, sticky='news', columnspan=4)

    def on_press(self, char):
        print(char)
        
# --- main ---

root = tk.Tk()
cal = Calc(root)
root.mainloop()
