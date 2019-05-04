
# date: 2019.05.03
# author: bartłomiej 'furas' Burek
# https://stackoverflow.com/questions/55956809/how-to-use-tkinter-tag-config-python-3-7-3/55960961#55960961

import tkinter as tk

# --- functions ---

def on_return(event):
    # -2c (-2chars) to skip `Return`

    # red color for last line
    text.tag_add('red_fg', 'end-2c linestart', 'end-2c')

    # blue color for last word
    text.tag_add('blue_fg', 'insert-2c wordstart', 'end-2c')


# --- main ---

root = tk.Tk()

text = tk.Text(root)
text.pack()

# tag's order can be important
text.tag_configure("red_fg", foreground="red")
text.tag_configure("blue_fg", foreground="blue")

root.bind("<Return>", on_return)

root.mainloop()
