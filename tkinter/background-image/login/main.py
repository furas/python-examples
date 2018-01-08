
# 
# https://stackoverflow.com/a/47983927/1832058
# 

import tkinter as tk

root = tk.Tk()
root.geometry('250x250')

img = tk.PhotoImage(file="hal_9000.gif")
img = img.subsample(1, 1)

background = tk.Label(root, image=img, bd=0)
background.pack(fill='both', expand=True)
background.image = img

# resize empty rows, columns to put other elements in center
background.rowconfigure(0, weight=100)
background.rowconfigure(3, weight=100)
background.columnconfigure(0, weight=100)
background.columnconfigure(3, weight=100)

name_label = tk.Label(background, text="Username")
name_label.grid(row=1, column=1, sticky='news')

name_entry = tk.Entry(background)## the Entry will let the user entre text inside the text box
name_entry.grid(row=1, column=2)

password_label = tk.Label(background, text="Password")
password_label.grid(row=2, column=1, sticky='news')

password_entry = tk.Entry(background, show="*")
password_entry.grid(row=2, column=2)

root.mainloop()
