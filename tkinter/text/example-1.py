#!/usr/bin/env python

#
# Get line of text from Text()
#
# http://effbot.org/tkinterbook/text.htm
# http://tcl.tk/man/tcl8.5/TkCmd/text.htm#M7
# 

import tkinter as tk

root = tk.Tk()

t = tk.Text(root)
t.pack()

t.insert('end', '''First line.
Second line.
Third line.''')

print(t.get('2.0', '3.0-1c'))
print(t.get('2.0', '2.0 lineend'))
print(t.get('2.0', '2.end'))

root.mainloop()
