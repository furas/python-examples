#!/usr/bin/env python3

# date: 2020.01.24
# 

import tkinter as tk
import pandas as pd
        
# --- functions ---

def on_click():
    val = selected.get()
    if val == 'all':
        print(df)
    else:        
        df2 = df[ df['TIME'] == val ]
        print(df2)

# --- main ---

df = pd.DataFrame({
    'TIME': ['00:00','00:00','01:00','01:00','02:00','02:00'],
    'A': ['a','b','c','d','e','f'],
    'B': ['x','x','y','y','z','z'],
})

root = tk.Tk()

values = ['all'] + list(df['TIME'].unique())
selected = tk.StringVar()
options = tk.OptionMenu(root, selected, *values)
options.pack()

button = tk.Button(root, text='OK', command=on_click)
button.pack()

root.mainloop()  

