
# date: 2019.04.16

import tkinter as tk
import random

def move():
    move_x = random.randint(-5, 5)
    move_y = random.randint(-5, 5)
    
    canvas.move(bird, move_x, move_y)
    x1,y1,x2,y2 = canvas.coords(bird)
    
    if x1 < 0:
        canvas.move(bird, -x1, 0)
    elif x2 >= WIDTH:
        canvas.move(bird, -x2 + WIDTH, 0)

    if y1 < 0:
        canvas.move(bird, 0, -y1)
    elif y2 >= HEIGHT:
        canvas.move(bird, 0, -y2 + HEIGHT)
        
    root.after(100, move)
    
def clicked(event):
    print("Hit!")

# --- main ---

SIZE = 50
WIDTH = 500
HEIGHT = 500

start_x = random.randint(0, WIDTH-SIZE)
start_y = random.randint(0, HEIGHT-SIZE)

root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

bird = canvas.create_rectangle(start_x, start_y, start_x+SIZE, start_y+SIZE, fill='green', tag='duck')

miss = canvas.tag_bind('duck', '<Button-1>', clicked)
canvas.focus_set()

move()

root.mainloop()
