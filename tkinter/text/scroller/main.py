
# date: 2019.08.04

import tkinter as tk
import json

data = {'name': "John", 'age': 31, 'city': "New York"}
text = json.dumps(data, indent=2)

root = tk.Tk()

# as default text is centered so I use `justify`
#lbl = tk.Label(root, text=text, font="Times32", justify='left')
#lbl.pack()

sb = tk.Scrollbar(root)
sb.pack(side='right', fill='y')

txt = tk.Text(root, font="Times32")
txt.pack()

txt.config(yscrollcommand=sb.set)
sb.config(command=txt.yview)

txt.insert('end', text)
txt.insert('end', text)
txt.insert('end', text)
txt.insert('end', text)
txt.insert('end', text)

root.mainloop()
