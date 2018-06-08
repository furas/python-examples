import pyglet

polygon_points = [10, 10, 30, 10, 30, 30, 10, 30] 
speed_x = 8
speed_y = 8

pause = False


window = pyglet.window.Window(width=640, height=480)

@window.event
def on_key_press(symbol, modifiers):
    global pause
    
    # on/off on press any key
    pause= not pause
    
    
@window.event
def on_draw():
    # clear screen to draw new frame
    window.clear()
    
    # draw polygon
    pyglet.graphics.draw(4,
        pyglet.gl.GL_POLYGON,
        ('v2i', polygon_points)
    )


def move_polygon(points, speed_x, speed_y):
    new_points = []
    
    while points:
        x = points.pop(0)
        y = points.pop(0)
        
        x += speed_x
        y += speed_y
        
        new_points.append(x)
        new_points.append(y)
        
    return new_points
    
    
def test_collision(points):    
    global speed_x
    global speed_y
    
    all_x = points[::2]
    all_y = points[1::2]
    
    if any(x <= 0 for x in all_x) or any(x >= 640 for x in all_x):
        speed_x = -speed_x # change direction in X

    if any(y <= 0 for y in all_y) or any(y >= 480 for y in all_y):
        speed_y = -speed_y # change direction in X
    
    
def update(dt):
    global polygon_points # use external variable instead creating local
    
    if not pause:
        # move polygon
        polygon_points = move_polygon(polygon_points, speed_x, speed_y)
        
        # check collision with border
        test_collision(polygon_points)
        
    # print(dt) time between frames - you can use it to make smother move


# execute `update` 60 times per second - it gives 60 FPS (Frames Per Second)    
pyglet.clock.schedule_interval(update, 1/60.0)    

pyglet.app.run()
