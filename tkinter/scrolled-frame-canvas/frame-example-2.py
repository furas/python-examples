import tkinter as tk
from scrolledframe import ScrolledFrame
import random
import string

# --- main ---

# random data
data = []
for row in range(30):
    row_data = []
    for col in range(20):
        row_data.append(random.choice(string.ascii_letters))
    data.append(row_data)

# ---

root = tk.Tk()              

# ---

# create scrolled frame
sf = ScrolledFrame(root, True, True)
sf.pack(fill='both', expand=True) # resize with window

# add widgets to scrolled frame - as parent you have to use `sf.inner` instead of `sf`
for row, row_data in enumerate(data):
    for col, txt in enumerate(row_data):
        l = tk.Label(sf.inner, text=txt)
        l.grid(row=row, column=col, padx=20)

# ---

root.mainloop()


