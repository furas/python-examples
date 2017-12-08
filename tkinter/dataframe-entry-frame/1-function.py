#!/usr/bin/env python

import pandas as pd
import tkinter as tk

# --- functions ---

def change(event, row, col):
    print(event.widget.get())
    df.iloc[row,col] = event.widget.get()
    print(df)
    
# --- main --    

df = pd.DataFrame([[1,2,3], [5,6,7], [101,102,103]])

root = tk.Tk()

rows, cols = df.shape
    
for r in range(rows):
    for c in range(cols):
        e = tk.Entry(root)
        e.insert(0, df.iloc[r,c])
        e.grid(row=r, column=c)
        # ENTER
        #e.bind('<Return>', lambda event, y=r, x=c: change(event, y,x))
        # ENTER on keypad
        #e.bind('<Return>', lambda event, y=r, x=c: change(event, y,x))

        e.bind('<KeyRelease>', lambda event, y=r, x=c: change(event, y,x))

root.mainloop()
