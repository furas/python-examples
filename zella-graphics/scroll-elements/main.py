from graphics import *
from random import randint

screen = GraphWin("Example", 500, 500)

# --- objects ---

line_1 = Text(Point(250, 500), "First line") 
line_2 = Text(Point(250, 500), "Second line") 
line_3 = Text(Point(250, 500), "Third line") 

# --- control objects ---

line_1.draw(screen)   # show first line at start 
move_line_1 = True   # move first line at start

move_line_2 = False  # don't move second line at start
move_line_3 = False  # don't move third line at start

while not screen.checkMouse():

    if move_line_1:
        # check if first line is on destination position
        if line_1.anchor.getY() <= 100:
            # stop first line
            move_line_1 = False
            
            # show second line
            line_2.draw(screen)
            
            # move second line
            move_line_2 = True
        else:
            # move first line
            line_1.move(0, -4)

    if move_line_2:
        # check if second line is on destination position
        if line_2.anchor.getY() <= 150:
            # stop second line
            move_line_2 = False
            
            # show third line
            line_3.draw(screen)
            
            # move third line
            move_line_3 = True
        else:
            # move second line
            line_2.move(0, -4)
            
    if move_line_3:
        # check if third line is on destination position
        if line_3.anchor.getY() <= 200:
            # stop third line
            move_line_3 = False
        else:
            # move third line
            line_3.move(0, -4)
            
    update(30) # 30 FPS (frames per second)
    
screen.close()
