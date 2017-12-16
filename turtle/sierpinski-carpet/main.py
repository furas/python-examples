#!/usr/bin/env python3

import turtle

# --- functions ---

def s(n, l):

    if n == 0: # stop conditions

        # draw filled rectangle

        turtle.color('black')
        turtle.begin_fill()
        for _ in range (4):
            turtle.forward(l)
            turtle.left(90)
        turtle.end_fill()

    else: # recursion

        # around center point create 8 smalles rectangles.
        # create two rectangles on every side 
        # so you have to repeat it four times

        for _ in range(4):
            # first rectangle
            s(n-1, l/3)    
            turtle.forward(l/3)

            # second rectangle
            s(n-1, l/3)    
            turtle.forward(l/3)

            # go to next corner
            turtle.forward(l/3)
            turtle.left(90)
            
        # update screen
        turtle.update()

# --- main ---    

# stop updating screen (to make it faster)
turtle.tracer(0) 

# start on screen click so it can be recorded with external program
#turtle.onscreenclick(lambda x,y:s(4, 400), 1)

# start
s(4, 400)

# event loop
turtle.mainloop()
