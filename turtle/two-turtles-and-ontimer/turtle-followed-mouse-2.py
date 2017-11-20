import turtle

# --- classes ---

class Follower:
    
    def __init__(self, x=0, y=0, dest=None):
        self.t = turtle.Turtle()
        self.t.speed(1)
        
        self.t.up()
        self.t.setposition(x, y)
        self.t.down()
        
        if dest is not None:
            self.destination(*dest)
            
    def destination(self, x, y):
        # turn head to destination point
        self.t.speed(0) # fastest
        self.t.setheading(self.t.towards(x, y))
        # move to destination point
        self.t.speed(1) # slowest
        self.t.goto(x, y)
        
    
    def get_position():
        return self.t.position()
        
# --- main ---

# create and start turtle
t = Follower(dest=(400, 200))

# set new destination on mouse click
turtle.onscreenclick(t.destination)

# star "the engine"
turtle.done()
