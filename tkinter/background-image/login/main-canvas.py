
# 
# https://stackoverflow.com/a/47983927/1832058
# 

import tkinter as tk

root = tk.Tk()
root.geometry('250x250')
root.title('Canvas')

canvas = tk.Canvas(root, width=250, height=250)
canvas.pack()

img = tk.PhotoImage(file='hal_9000.gif')

canvas.create_image((0, 0), image=img, anchor='nw')

canvas.create_text((10, 100), text='Username', anchor='w', fill='white', font=('Arial', 10))
canvas.create_text((10, 150), text='Password', anchor='w', fill='white', font=('Arial', 10))

name_entry = tk.Entry(canvas)
password_entry = tk.Entry(canvas, show='*')

canvas.create_window((240, 100), window=name_entry, anchor='e')
canvas.create_window((240, 150), window=password_entry, anchor='e')

root.mainloop()
