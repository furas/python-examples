import turtle as t
from tkinter import messagebox

def on_forward():
    val = t.textinput('Forward', "How much: ")
    if val:
        try:
            val = int(val)
            t.forward(val)
        except ValueError:
            messagebox.showinfo('Error', 'Wrong value')
    t.listen()

def on_backward():
    val = t.textinput('Backward', "How much: ")
    if val:
        try:
            val = int(val)
            t.backward(val)
        except ValueError:
            messagebox.showinfo('Error', 'Wrong value')
    t.listen()
    
def on_left():
    val = t.textinput('Left', "How much: ")
    if val:
        try:
            val = int(val)
            t.left(val)
        except ValueError:
            messagebox.showinfo('Error', 'Wrong value')
    t.listen()
    
def on_right():
    val = t.textinput('Right', "How much: ")
    if val:
        try:
            val = int(val)
            t.right(val)
        except ValueError:
            messagebox.showinfo('Error', 'Wrong value')
    t.listen()

def on_exit():
    t.bye()  

t.showturtle()

# assign functions to keys
t.onkeypress(on_forward, 'f')
t.onkeypress(on_backward, 'b')
t.onkeypress(on_left, 'l')
t.onkeypress(on_right, 'r')
t.onkeypress(on_exit, 'e')

# catch key presses in main window
t.listen()

# run loop which will execute functions 
t.mainloop()
