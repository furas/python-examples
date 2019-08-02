
# date: 2019.07.24
# https://stackoverflow.com/questions/57189326/unexpected-typeerror-while-using-setworldcoordinates/57189988#57189988

import tkinter as tk
import turtle

root = tk.Tk()

cv = tk.Canvas(root, width=200, height=200)
cv.pack() # <-- or cv.grid() but not cv.place() / needed by setworldcoordinates and _window_size

print([cv['width'], cv['height']]) # strings ['200', '200']
print([cv.winfo_width(), cv.winfo_height()]) # integers [1, 1]

screen = turtle.TurtleScreen(cv)

print([cv['width'], cv['height']]) # strings ['200', '200']
print([cv.winfo_width(), cv.winfo_height()]) # integers ['202', '202']

screen.setworldcoordinates(-50, -50, 50, 50)
# error when there is no `cv.pack()`

