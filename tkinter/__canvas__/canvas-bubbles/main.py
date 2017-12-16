import tkinter as tk
import random

class Bubble():
    
    def __init__(self, canvas, x, y, size, color='red', start_offset_y=0):
        self.canvas = canvas
        
        self.x = x 
        self.y = y + start_offset_y
        
        self.start_x = x
        self.start_y = y
        
        self.size = size
        self.color = color
        
        rect = [self.x, self.y, self.x+self.size, self.y+self.size]
        self.circle = canvas.create_oval(rect, outline=color, fill=color)
        
    def move(self):
        x_vel = random.randint(-5, 5)
        y_vel = -5
    
        self.canvas.move(self.circle, x_vel, y_vel)
        coordinates = self.canvas.coords(self.circle)
    
        self.x = coordinates[0]
        self.y = coordinates[1]

        # if outside screen move to start position
        if self.y < -self.size:
            self.x = self.start_x
            self.y = self.start_y
            self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)
        
def move():
    for item in bubbles:
        item.move()

    window.after(33, move)
        
# --- main ---

start_x = 125-20
start_y = 500-40

window = tk.Tk()
window.geometry("250x500")

canvas = tk.Canvas(window, width=2500, height=500)
canvas.grid(row=0, column=0, sticky='w')

bubbles = []
for i in range(10):
    if i % 2 == 0:
        color = 'red'
    else:
        color = 'green'
        
    offset = i * 50
    b = Bubble(canvas, start_x+10, start_y, 20, color, offset)
    bubbles.append(b)
    
coord = [start_x, start_y, start_x+40, start_y+40]
rect = canvas.create_rectangle(coord, outline="Blue", fill="Blue")

move()

window.mainloop ()
