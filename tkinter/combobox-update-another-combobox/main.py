
# date: 2019.04.23

from tkinter import *
from tkinter.ttk import Combobox

data = {
    "EMEA": [1105,1106],
    "ASIA": [3565,2445, 126464, 1145454],
    "AMERICA": [56464 ,5679, 55346],
}


def on_select(event):
    print(event)
    selecte_value = event.widget.get()
    if selecte_value in data:
        cb2['values'] = data[selecte_value]
    else:
        cb2['values'] = all_values

country = list(data.keys())
all_values = sorted(sum(data.values(), []))

window = Tk()

cb1 = Combobox(window, values=country)
cb1.bind('<<ComboboxSelected>>', on_select)
cb1.bind('<Return>', on_select) # pressed ENTER
cb1.pack()

cb2 = Combobox(window, values=all_values)
cb2.pack()

window.mainloop()
