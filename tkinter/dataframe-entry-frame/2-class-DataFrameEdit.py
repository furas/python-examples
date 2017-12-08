#!/usr/bin/env python

import pandas as pd
import tkinter as tk

class DataFrameEdit(tk.Frame):
    
    def __init__(self, master, data, *args):
        super().__init__(master, *args)
        
        self.data = data
        self.rows, self.cols = data.shape

        for r in range(self.rows):
            for c in range(self.cols):
                e = tk.Entry(self)
                e.insert(0, self.data.iloc[r,c])
                e.grid(row=r, column=c)
                # ENTER
                #e.bind('<Return>', lambda event, y=r, x=c: self.change(event, y,x))
                # ENTER on keypad
                #e.bind('<Return>', lambda event, y=r, x=c: self.change(event, y,x))
        
                e.bind('<KeyRelease>', lambda event, y=r, x=c: self.change(event, y,x))
            
    def change(self, event, row, col):
        self.data.iloc[row,col] = event.widget.get()
        print(self.data)
        
        
# --- main --    

df1 = pd.DataFrame([[1,2,3], [5,6,7], [101,102,103]])
df2 = pd.DataFrame([['a','x'], ['b','y'],['c','z']])

root = tk.Tk()

tk.Label(root, text='DataFrame #1').pack()
DataFrameEdit(root, df1).pack()

tk.Label(root, text='DataFrame #2').pack()
DataFrameEdit(root, df2).pack()

root.mainloop()
