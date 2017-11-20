import turtle 

#
# Lévy C curve
#
# https://en.wikipedia.org/wiki/Lévy_C_curve
#

# --- functions ---

def cCurve(t, x1, y1, x2, y2, level):

    if level == 0:
        # draw line x1, y1, x2, y2
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) //2
        ym = (x2 + y1 + y2 - x1) //2
        cCurve(t, x1 ,y1 ,xm, ym, level -1)
        cCurve(t, xm, ym, x2, y2, level -1)
        
# --- main ---
            
level = int(input('Enter the level(0 or greater): ' ))

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

cCurve(t, 50, -50, 50, 50, level)

turtle.done()
