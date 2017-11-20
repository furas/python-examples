import turtle

# --- functions ---

def move_t1():
    # first turtle moves a little
    t1.left(10)  
    t1.forward(10)
    
    # repeat it after 100ms
    turtle.ontimer(move_t1, 100)

def move_t2():
    # second turtle moves a little
    t2.right(10)  
    t2.forward(10)
    
    # repeat it after 100ms
    turtle.ontimer(move_t2, 100)

# --- main ---

# create two turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# start moving both turtles
move_t1()
move_t2()

# star "the engine"
turtle.done()
