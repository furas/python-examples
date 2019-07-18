
# 2019.07.18

import tkinter as tk

def set_bold():
    try:
        textbox.tag_add('bold', 'sel.first', 'sel.last')
    except Exception as ex:
        # text not selected
        print(ex)

def set_red():
    try:
        textbox.tag_add('red', 'sel.first', 'sel.last')
    except Exception as ex:
        # text not selected
        print(ex)
    
root = tk.Tk()

textbox = tk.Text(root)
textbox.pack()

textbox.tag_config('bold', font=('Arial', 10, 'bold'))
textbox.tag_config('red', foreground='red')

button1 = tk.Button(root, text='Bold', command=set_bold)
button1.pack()

button2 = tk.Button(root, text='Red', command=set_red)
button2.pack()

root.mainloop()
