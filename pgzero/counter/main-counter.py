import pgzrun

counter = 0

def draw():
    screen.clear()
    screen.draw.text("Counter: " + str(counter), (10, 10))

def timer():
    global counter
    counter += 1

clock.schedule_interval(timer, 0.5)
pgzrun.go()
