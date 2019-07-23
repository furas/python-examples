
# date: 2019.07.22
# https://stackoverflow.com/questions/57143621/tkinter-button-widget-inside-another-button-widget-tkinter
#
# Linux has problem to click B1 when move from B2 to B1.
# Windows has problem to display buttons.

import tkinter as tk

def set_focus(event):
    print(event.widget)
    event.widget.focus()

root=tk.Tk()

b1 = tk.Button(root, height=7, width=13, bg='green', command=lambda:print('B1'))
b1.place(x=0, y=0)
b1.bind('<Enter>', set_focus)

b2 = tk.Button(b1, height=3, width=5, bg='red', command=lambda:print('B2'))
b2.place(x=0, y=0)
b2.bind('<Enter>', set_focus)

root.mainloop()
