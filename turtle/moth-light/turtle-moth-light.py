import turtle
import random

# --- classes ---


class Moth:
    
    def __init__(self, pos, dest=None):
        '''create and initiate moth'''
        
        # define turtle 
        self.t = turtle.Turtle()
        self.t.speed(0)

        # it is needed to execute `ontimer`
        self.screen = turtle.Screen()
        
        # remember destination
        self.dest = dest

        # at start it is not fly
        self.is_flying = False        

        # move to start position 
        #(it will use self.dest so it has to be after `self.dest = dest`)
        self.move(pos)
        
        # if destination is set then fly to it
        # (currently it is in `move()`)
        #if self.dest is not None:
        #    self.move_to_light(self.dest)

    def move(self, pos):
        '''move to start position immediately (without steps)'''
        
        # move to new position
        self.t.up()
        self.t.setposition(pos)
        self.t.down()

        # start flying
        if self.dest is not None:
            self.move_to_light(self.dest)

    def move_to_random_place(self):
        x = random.randint(-800, 800)
        y = random.randint(-300, 300)
        self.move((x,y))
        
    def move_to_light(self, dest):
        '''start flying to light'''
        
        # set new destination position
        self.dest = dest

        # turn head to destination position
        self.t.setheading(self.t.towards(self.dest))

        # if not flying yet then start flying
        if not self.is_flying:
            self.is_flying = True
            self._fly()

    def _fly(self):
        '''fly to light with 10px steps (using ontimer)'''
        STEP = 10
        
        # get distance to light
        distance = self.t.distance(self.dest)
        
        # make one step or stop
        if distance > STEP:
            self.t.forward(STEP)
        elif distance > 0: # you can use ie. > 3 to stop 3px before light
            self.t.forward(distance)
            
            # you can stop flying
            #self.is_flying = False
            
            # or you move to new random place
            self.move_to_random_place()
            
        #else do nothing
        
        # if still flying then repeat function after 100ms
        if self.is_flying:
            self.screen.ontimer(self._fly, 100)

    def get_position():
        '''get current position'''
        return self.t.position()

# --- functions ---

def move_light(x, y):
    global light
    
    # get mouse position as new light
    light = (x, y)
  
    # change destination for all moths  
    for m in moths:
        m.move_to_light(light)

def move_moths(x, y):
    # move all moths to random places
    for m in moths:
        # put one moth in random places
        m.move_to_random_place()

# --- main ---

# list to keep all moths
moths = []

# ligth position at start 
# (later you can change it clicking on screen)
# (there is no object which show light on screen)
light = (0, 0)

# create some moths in random places
for _ in range(5):
    # put moth in random places
    x = random.randint(-800, 800)
    y = random.randint(-300, 300)
    m = Moth( (x, y), dest=light)

    # or use `move_to_random_place()`
    #m = Moth( (0, 0), dest=light)
    #m.move_to_random_place()
    
    # remember moth on list
    moths.append(m)

# mouse LEFT button will move light
turtle.onscreenclick(move_light)

# mouse RIGHT button will move moths to random places
turtle.onscreenclick(move_moths, 3)

# star "the engine"
turtle.done()
