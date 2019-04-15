
# date: 2019.04.15

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

filename = filedialog.askopenfilename(title="Select file")
print('filename:', filename)

data = open(filename).read()
print(data)

label = tk.Label(root, text=filename)
label.pack()

root.mainloop()

