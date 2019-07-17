import turtle
import tkinter as tk

def test(value):
    print("clicked", value)
    label['text'] = str(value)

canvas = turtle.getcanvas()
parent = canvas.master

label = tk.Label(parent, text="???")
canvas.create_window((0, -30), window=label)

for x in range(10):
    text = 'Button {}'.format(x)
    button = tk.Button(parent, text=text, command=(lambda val=x:test(val)))
    canvas.create_window((0, x*30), window=button)

turtle.done()
