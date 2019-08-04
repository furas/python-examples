
# date: 2019.07.24
# https://stackoverflow.com/questions/57166574/tkinter-gui-and-plots-and-threading

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# --- functions ---

def function_plot():
    #global canvas
    #global df
    
    data = {
        'Country': ['USA', 'UK', 'CAN', 'GER', 'FR', 'FIN', 'SWE'],
        'GDP_Per_Capita': [45000, 49000, 42000,56000, 47000, 58000, 57000]
    }
    
    df = pd.DataFrame(data, columns = ['Country', 'GDP_Per_Capita'])
    df = df[['Country', 'GDP_Per_Capita']].groupby('Country').sum()
    print(df)
    
    item = df['GDP_Per_Capita'].plot(kind='bar')

    canvas = FigureCanvasTkAgg(item.figure, root)
    canvas.get_tk_widget().pack()

# --- main ---

root = tk.Tk()
root.geometry('400x400')

menu = tk.Menu(root)
fileMenu = tk.Menu(root)
fileMenu.add_cascade(label="Open Log File")
fileMenu.add_cascade(label="Reset Status")
menu.add_cascade(label="File", menu=fileMenu)

helpMenu = tk.Menu(root)
helpMenu.add_cascade(label="Help Document")
helpMenu.add_cascade(label="About This Program")
menu.add_cascade(label="Help", menu=helpMenu)

root.configure(menu=menu, bg="blue")

b1 = tk.Button(root, text="Click Me!", command=function_plot)
b1.pack()

root.mainloop()
