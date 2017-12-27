import tkinter as tk
import random

def myfunction(event):
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 400)
    x2 = random.randint(0, 400)
    y2 = random.randint(0, 400)
    canvas.create_line(x1, y1, x2, y2)

root = tk.Tk()
root.title('Picasso')

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.bind('q', myfunction)

root.mainloop()
