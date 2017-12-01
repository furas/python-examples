from tkinter import *

def check():
    widget = root.focus_get()
    if isinstance(widget, Entry):
        print('e1:', widget == e1)
        print('e2:', widget == e2)
        print('text:', widget.get())
    else:
        print("Not Entry")

root = Tk()

e1 = Entry(root) #  Entry for year
e1.pack()

e2 = Entry(root) #  Entry for Month
e2.pack()

b = Button(root, text='Check', command=check) 
b.pack()

mainloop()
