
# date: 2019.07.23
# https://stackoverflow.com/questions/57161644/how-to-pop-up-an-on-screen-keyboard-to-enter-some-data-in-an-entry-gadget-in-tki/57162755?noredirect=1#comment100841209_57162755

import tkinter as tk

def create_keypad(root):
    keypad = tk.Frame(root)

    for y in range(3):
        for x in range(3):
            val = y*3 + x
            text = str(val)
            b = tk.Button(keypad, text=text, command=lambda txt=text:insert_text(txt))
            b.grid(row=y, column=x, sticky='news')

    x = tk.Button(keypad, text='Hide', command=hide_keypad)
    x.grid(row=10, column=0, columnspan=3, sticky='news')
    
    return keypad


def insert_text(text):
    target.insert('end', text)
    
def show_keypad(widget):
    global target
    target = widget
    
    keypad.place(relx=0.5, rely=0.5, anchor='c')
    
def hide_keypad():
    global taget
    target = None

    keypad.place_forget()


root = tk.Tk()
root.geometry('600x400')

keypad = create_keypad(root)
target = None

f = tk.Frame(root)
f.pack()

e1 = tk.Entry(f)
e1.grid(row=0, column=0)
b1 = tk.Button(f, text='Keypad', command=lambda:show_keypad(e1))
b1.grid(row=0, column=1)

e2 = tk.Entry(f)
e2.grid(row=1, column=0)
b2 = tk.Button(f, text='Keypad', command=lambda:show_keypad(e2))
b2.grid(row=1, column=1)


root.mainloop()


