import turtle

# --- main ---

# create two turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# start moving turtles alternately
for _ in range(36):
    
    # first turtle moves a little
    t1.left(10)  
    t1.forward(10)
    
    # second turtle moves a little
    t2.right(10)  
    t2.forward(10)

# star "the engine"
turtle.done()
