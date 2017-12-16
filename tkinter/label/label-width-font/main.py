#If you display text in the label, these options define the size of the label in text units. If you display bitmaps or images instead, they define the size in pixels (or other screen units)

import tkinter as tk

root = tk.Tk()

f = None

l1 = tk.Label(root, text='Hello', width=7, fg='white', bg='blue', font=f)

f = ('HelveticaNeue Light', 12)
l2 = tk.Label(root, text='Hello', width=7, fg='white', bg='green', font=f)

f = ('HelveticaNeue Light', 12, 'bold')
l3 = tk.Label(root, text='Hello', width=7, fg='white', bg='red', font=f)


l1.grid()
l2.grid()
l3.grid()

root.mainloop()
