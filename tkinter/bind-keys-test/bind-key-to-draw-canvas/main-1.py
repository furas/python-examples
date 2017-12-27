import tkinter as tk

def myfunction(event):
    canvas.create_line(0,0,400,400)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.bind('q', myfunction)

root.mainloop()
