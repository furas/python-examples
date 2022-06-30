# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.29
# [python - how erase the last character of one widget/text in tkinter - Stack Overflow](https://stackoverflow.com/questions/72807497/how-erase-the-last-character-of-one-widget-text-in-tkinter/)

import tkinter as tk

# --- functions ---

def on_click():
    print('Entry:', entry.get())
    entry.delete(len(entry.get())-1)

    print('StringVar:', string_var.get())
    string_var.set( string_var.get()[:-1] )

    print('Text:', text.get('0.0', 'end'))
    text.delete('end-2c', 'end')

# --- main ---

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

string_var = tk.StringVar()
entry_var = tk.Entry(root, textvar=string_var)
entry_var.pack()

text = tk.Text(root)
text.pack()

button = tk.Button(root, text='DELETE', command=on_click)
button.pack()

root.mainloop()

