from turtle import Turtle, Screen

def key_add(value):
    if value in 'wasd':
        keys.append(value)
    
def key_remove(value):
    if value in keys: 
        keys.remove(value)

def move_it():
    if keys:
        k = keys[-1]
        if k == 'w':
            move.forward(5)
        elif k == 'a':
            move.left(5)
        elif k == 's':
            move.back(5)
        elif k == 'd':
            move.right(5)
    screen.ontimer(move_it, 25)
    
keys = []

move = Turtle()

screen = Screen()
move.speed(0)

screen.onkeypress(lambda:key_add('w'), "w")
screen.onkeypress(lambda:key_add('a'), "a")
screen.onkeypress(lambda:key_add('s'), "s")
screen.onkeypress(lambda:key_add('d'), "d")
screen.onkeyrelease(lambda:key_remove('w'), 'w')
screen.onkeyrelease(lambda:key_remove('a'), 'a')
screen.onkeyrelease(lambda:key_remove('s'), 's')
screen.onkeyrelease(lambda:key_remove('d'), 'd')

screen.listen()
screen.ontimer(move_it, 25)

screen.mainloop()
