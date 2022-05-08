# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.03

# doc: https://docs.python.org/3/library/dialog.html

# python -m tkinter.simpledialog

# tkinter.simpledialog
#   askstring(title, prompt, **kw)
#   askinteger(title, prompt, **kw)
#   askfloat(title, prompt, **kw)

import tkinter as tk
import tkinter.simpledialog

# source code in file
#print( tkinter.simpledialog.__file__ )

# --- 

def show_dialogs():
    # it doesn't get `parent` as first argument but it needs to use `parent=`
    
    result = tkinter.simpledialog.askstring('Example askstring ', 'Write text:', parent=root)
    print('result:', result, type(result))
    
    result = tkinter.simpledialog.askinteger('Example askinteger', 'Write integer number:', parent=root)
    print('result:', result, type(result))
    
    result = tkinter.simpledialog.askfloat('Example askfloat', 'Write float number:', parent=root)
    print('result:', result, type(result))

    #result = tkinter.simpledialog.askstring('Example askstring ', 'Write password:', show="?", parent=root)  # you can set any char (but not 2 chars)
    result = tkinter.simpledialog.askstring('Example askstring ', 'Write password:', show="*", parent=root)    
    print('result:', result, type(result))

# --- main ---

root = tk.Tk()

button = tk.Button(root, text='Show Dialogs', command=show_dialogs)
button.pack()

root.mainloop()

