
# date: 2019.08.23
# 

import tkinter as tk

def return_entry(event=None):
    '''
    'bind' sends 'event' but 'command=' doesn't send 'event' 
    so function will get 'None' and it can't use 'event.widget'
    '''
    content = entry.get()
    print(content)


root = tk.Tk()

entry1 = tk.Entry(root)
entry1.pack()

entry1.bind('<Return>', return_entry)

button = tk.Button(root, text='OK', command=return_entry)
button.pack()

root.mainloop()


