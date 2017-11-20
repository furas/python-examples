import turtle

# --- classes ---

class TurtleOne:
    
    def __init__(self, pos):
        self._turtle = turtle.Turtle()

        # move to initial position
        self._turtle.speed(0) # fastest
        self._turtle.up()
        self._turtle.setposition(pos)
        self._turtle.down()
            
    def move(self, pos):
        # turn head to destination point
        self._turtle.speed(0) # fastest
        self._turtle.setheading(self._turtle.towards(pos))
        # move to destination point
        self._turtle.speed(1) # slowest
        self._turtle.goto(pos)
    
    def get_position():
        return self._turtle.position()
        
class TurtleTwo(turtle.Turtle):
    
    def __init__(self, pos):
        super().__init__()
        
        # move to initial position
        self.speed(0) # fastest
        self.up()
        self.setposition(pos)
        self.down()
        
    def move(self, pos):
        # turn head to destination point
        self.speed(0) # fastest
        self.setheading(self.towards(pos))
        # move to destination point
        self.speed(1) # slowest
        self.goto(pos)
    
    def get_position():
        return self.position()
        
# --- main ---


# create and start turtle
t = Follower(dest=(400, 200))

# set new destination on mouse click
turtle.onscreenclick(t.destination)

# star "the engine"
turtle.done()
