import pyglet

polygon_points = (10, 15, 30, 35, 50, 15)

window = pyglet.window.Window()

@window.event
def on_draw():
    # clear screen to draw new frame
    window.clear()
    
    # draw polygon
    pyglet.graphics.draw(3,
        pyglet.gl.GL_POLYGON,
        ('v2i', polygon_points)
    )

def update(dt):
    global polygon_points # use external variable instead creating local
    
    # move every point in polygon a little
    polygon_points = tuple(x+1 for x in polygon_points)
    
    # print(dt) time between frames - you can use it to make smother move

# execute `update` 60 times per second - it gives 60 FPS (Frames Per Second)    
pyglet.clock.schedule_interval(update, 1/60.0)    

pyglet.app.run()
