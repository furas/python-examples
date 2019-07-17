
# date: 2019.07.09
# https://stackoverflow.com/questions/56960444/how-to-make-python-text-into-a-button-in-python-turtle/56960881

import turtle
import tkinter as tk

def show_cat():
    label = tk.Label(canvas.master, text="HELLO", font=("Times New Roman", 120, "bold"))
    canvas.create_window(0, -300, window=label)
    canvas.create_text(0, 300, text="WORLD!", fill="red", font=("Times New Roman", 120, "bold"))


screen = turtle.Screen()
screen.setup(800,800)

canvas = screen.getcanvas()

button = tk.Button(canvas.master, text="Click Me", command=show_cat)
canvas.create_window(0, 0, window=button)

turtle.mainloop()
