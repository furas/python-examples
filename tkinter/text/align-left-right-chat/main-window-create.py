#!/usr/bin/env python3 

# date: 2019.12.14
# 

import tkinter as tk 
import tkinter.scrolledtext as ScrolledText

root = tk.Tk()
#text_widget = tk.Text()
text_widget = ScrolledText.ScrolledText()
text_widget.pack(fill='both', expand=True)

label1 = tk.Label(text_widget, text="Hello\nWorld!!!", background='#d0ffff', justify='left', padx=10, pady=5)
label2 = tk.Label(text_widget, text="Hello\nWorld!!!", background='#ffffd0', justify='left', padx=10, pady=5)
label3 = tk.Label(text_widget, text="Hello\nWorld!!!", background='#d0ffff', justify='left', padx=10, pady=5)

text_widget.tag_configure('tag-left', justify='left')
text_widget.tag_configure('tag-right', justify='right')


text_widget.insert('end', '\n')
text_widget.window_create('end', window=label1)

text_widget.insert('end', '\n ', 'tag-right') # space to move right Label
text_widget.window_create('end', window=label2)

text_widget.insert('end', '\n')
text_widget.window_create('end', window=label3)

root.mainloop()
