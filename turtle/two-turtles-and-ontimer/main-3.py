import turtle

# --- classes ---

class T800:
    
    def __init__(self, x, y):
        self.t = turtle.Turtle()
        self.t.speed(0)
        
        self.t.up()
        self.t.goto(x, y)
        self.t.down()
        
        self.running = True
        
    def start(self):
        self.running = True
        self.move()
        
    def move(self):
        if self.running:
            # moves a little
            self.t.left(10)  
            self.t.forward(10)
            self.t.left(10)  
            self.t.forward(10)
        
            # repeat it after 100ms
            screen.ontimer(self.move, 100)

    def stop(self):
        self.running = False
        
# --- functions ---

def on_click(x, y):
    t = T800(x, y)
    t.start()
    turtles.append(t)
    
def on_right_click(x, y):
    for t in turtles:
        if t.running:
            t.stop()
        else:
            t.start()
            
# --- main ---

turtles = []

screen = turtle.Screen()

# create and start two turtles
t = T800(100, 0)
t.move()
turtles.append(t)

t = T800(-100, 0)
t.move()
turtles.append(t)

# create turtle on mouse click
turtle.onscreenclick(on_click)
turtle.onscreenclick(on_right_click, 3)

# star "the engine"
turtle.done()
