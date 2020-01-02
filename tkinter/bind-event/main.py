#!/usr/bin/env python3 

# date: 2019.12.22
#https://stackoverflow.com/questions/59441994/how-to-generate-tab-key-even-when-enter-key-pressed-in-tkinter-python



import tkinter as tk

root = tk.Tk()

e1 = tk.Entry(root)
e1.pack()
e2 = tk.Entry(root)
e2.pack()
print(e1)
#root.call('bind .!entry <Return> {event generate %W <Tab>}')
#bind .w <Return> {event generate %W <Tab>}
e1.bind('<Return>', 'event generate %W <Tab>')
#e2.bind('<Return>', 'event generate %W <Tab>')
#e2.bind('<Return>', lambda x:root.event_generate('<Tab>'))
#e2.bind('<Return>', '<Tab>')
e2.bind('<Return>', root.bind_all("<Tab>")) # doesn't work on Linux ?

root.mainloop()
