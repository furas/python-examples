import tkinter as tk

# date: 2019.05.01
# author: Bartłomiej 'furas' Burek

# You have to add something to canvas to use scrollbar.
# You have to use `scrollregion=` after you put items in canvas
#  or you can use `after` to do it after tkinter shows window.

#def resize():
#    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()

frame1 = tk.Frame(root, width=900, height=800)
frame1.pack(expand=True, fill='both')

canvas = tk.Canvas(frame1, width=900, height= 900)
canvas.pack(side='left', fill='both', expand=True)

vsb = tk.Scrollbar(frame1, orient='vertical')
vsb.pack(fill='y', side='right', expand=False)
vsb.configure(command=canvas.yview)

item_1 = tk.Frame(canvas, bg='red', width=500, height=500)
canvas.create_window(0, 0, window=item_1, anchor='nw')

item_2 = tk.Frame(canvas, bg='green', width=500, height=500)
canvas.create_window(500, 500, window=item_2, anchor='nw')

canvas.configure(yscrollcommand=vsb.set, scrollregion=canvas.bbox("all"))

#root.after(100, resize)

root.mainloop()
