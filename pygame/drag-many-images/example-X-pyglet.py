#!/usr/bin/env python

# date: 2019.07.11
# https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs

# It drags two images at the same time, You can click in any place.

import pyglet

window = pyglet.window.Window(width=800, height=600)

batch = pyglet.graphics.Batch()
items = [
    pyglet.sprite.Sprite(pyglet.resource.image('hal_9000.jpg'), x=200, y=100, batch=batch),
    pyglet.sprite.Sprite(pyglet.resource.image('hal_9000.jpg'), x=400, y=300, batch=batch),
]

@window.event
def on_draw():
    #window.clear()
    
    #RED = (213, 43, 67)
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', [0,0, 800,0, 800,600, 0,600]), ('c3B', [213,43,67, 213,43,67, 213,43,67, 213,43,67]))    
    
    batch.draw()
    
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    for i in items:
        i.x += dx
        i.y += dy

pyglet.app.run()

