import turtle

# --- functions ---

def onmousemove(callback):
    cv = turtle.getcanvas()
    cv.bind('<Motion>', callback)

# --- test ---
    
def test(event):
    print('test on mouse move', event)
    print('x, y, state:', event.x, event.y, event.state)
    
onmousemove(test)

turtle.done()
