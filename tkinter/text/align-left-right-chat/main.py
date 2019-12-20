#!/usr/bin/env python3 

# date: 2019.12.14
# 

import tkinter as tk 
import tkinter.scrolledtext as ScrolledText

root = tk.Tk()
#text_widget = tk.Text()
text_widget = ScrolledText.ScrolledText()
text_widget.pack(fill='both', expand=True)

text_widget.tag_configure('tag-center', justify='center')
text_widget.tag_configure('tag-left', justify='left')
text_widget.tag_configure('tag-right', justify='right', background='red')

text_widget.insert('end', 'Hello\nWorld!!!\n', 'tag-center')
text_widget.insert('end', 'Hello\nWorld!!!\n', 'tag-left')
text_widget.insert('end', 'Hello\nWorld!!!\n', 'tag-right')

root.mainloop()
