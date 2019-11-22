#!/usr/bin/env python3

# date: 2019.10.22
# Sprites have to be assigned to global or class variables to display it

import pyglet
import random

# --- classes ---

class Board:

    def __init__(self):
        self.my_batch = pyglet.graphics.Batch()
        self.all_images = [
            pyglet.image.load("square-1.png"),
            pyglet.image.load("square-2.png"),
            pyglet.image.load("square-3.png"),
            pyglet.image.load("square-4.png"),
            pyglet.image.load("square-5.png"),
        ]
        self.all_sprites = []
        self.render()
        
    def render(self):
        self.all_sprites = []
        for y in range(1, 600, 50):
            for x in range(2, 800, 50):
                i = random.choice(self.all_images)
                s = pyglet.sprite.Sprite(i, x, y, batch=self.my_batch)
                self.all_sprites.append(s)  # <-- try without this line and you will no see image
        
    def draw(self):
        self.my_batch.draw()
            
# --- main ---
            
window = pyglet.window.Window(width=800, height=600)
print(window.get_size())
island = Board()

@window.event()
def on_draw():
    window.clear()
    island.draw()
    
def update(dt):
    island.render()
    
pyglet.clock.schedule_interval(update, 0.1)

pyglet.app.run()    
