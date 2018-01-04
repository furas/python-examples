import tkinter as tk

root = tk.Tk()
root.title("Test")

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

for x in range(4, 100, 10):
    for y in range(4, 100, 10):
        canvas.create_oval((x, y, x, y), fill="red")

root.update()

root.mainloop()
