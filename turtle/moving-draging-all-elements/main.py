import turtle

t = turtle.Turtle()

# --- move all elements ---

def move(offset_x, offset_y):

    canvas = turtle.getcanvas() # `turtle`, not `t`
    for element_id in canvas.find_all():
        canvas.move(element_id, offset_x, offset_y)

# --- move all on draging turtle ---

old_x = 0
old_y = 0

def on_click(x, y):
    global old_x, old_y

    old_x = x
    old_y = y
    
    print(x, y)
    
def on_drag(x, y):
    global old_x, old_y
    
    move(x-old_x, old_y-y)
    
    old_x = x
    old_y = y

t.onclick(on_click)
t.ondrag(on_drag)

# --- example ---

# draw something 

for a in range(8):
    for _ in range(8):
        t.left(45)
        t.fd(20)
    t.right(45)
    t.up()
    t.fd(60)
    t.down()

# move

move(300, 50)

# ---

turtle.done() # `turtle`, not `t`
