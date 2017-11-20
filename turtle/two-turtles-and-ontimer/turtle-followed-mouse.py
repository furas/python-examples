import turtle

# --- classes ---

class Follower:
    
    def __init__(self, x=0, y=0, dest=None):
        self.t = turtle.Turtle()
        self.t.speed(0)
        
        self.t.up()
        self.t.goto(x, y)
        self.t.down()
        
        if dest is None:
            # use start point as destination point
            self.destination(x, y)
        else:
            self.destination(*dest)
            
        # it is needed by `move` to execute `ontimer`
        self.screen = turtle.Screen()

        # start moving
        self.move()

    def destination(self, x, y):
        # set new destination point
        self.dest = (x, y)
        # turn to destination point
        self.t.setheading(self.t.towards(self.dest))
        
    def move(self):

        length = self.t.distance(self.dest)
        
        if length > 10:
            self.t.forward(10)
        elif length > 0:
            self.t.forward(length)
        #else don't move
        
        # repeat it after 100ms
        self.screen.ontimer(self.move, 100)

    # --- not used in example ---
    
    def get_position():
        return self.t.position()
        
# --- main ---

# create and start turtle
t = Follower(dest=(400, 200))

# set new destination on mouse click
#turtle.onscreenclick(on_click)
turtle.onscreenclick(t.destination)

# star "the engine"
turtle.done()
