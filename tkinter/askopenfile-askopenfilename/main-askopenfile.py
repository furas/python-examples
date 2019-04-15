
# date: 2019.04.15

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

file_object = filedialog.askopenfile(title="Select file")
print('file_object:', file_object)
print('file_object.name:', file_object.name)

data = file_object.read()
print(data)

label = tk.Label(root, text=file_object.name)
label.pack()

root.mainloop()

