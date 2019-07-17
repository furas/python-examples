
# date: 2019.07.10
# https://stackoverflow.com/questions/56963013/tkintertable-data-how-to-update/56963101#56963101

import tkinter as tk
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

data={'1': {'Klasa':'6A', 'E Hene': 1, 'E Marte': 2,'E Merkurre':3,'E Enjte':4,'E Premte':5},
      '2': {'Klasa':'', 'E Hene': 1, 'E Marte': 2,'E Merkurre':3,'E Enjte':4,'E Premte':5}}


def update_data(event=None):
    print("update_data")

    nk = "3"
   
    model.addRow(key=nk, Klasa="333")
    table.redraw()
    

master = tk.Tk()

tframe = tk.Frame(master)
tframe.pack(fill='both', expand=True)

model = TableModel()
table = TableCanvas(tframe, model=model)

table.createTableFrame()
model.importDict(data)

master.after(1000, update_data)

master.mainloop()


