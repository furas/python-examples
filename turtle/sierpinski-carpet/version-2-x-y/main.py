
# https://stackoverflow.com/questions/57133776/recursive-carpet-python-turtle/57136958#57136958

import turtle

def drawTriangle(points, color, myTurtle, show=False):
    if show:
        print('DRAW:', points)

    myTurtle.fillcolor(color)
    myTurtle.up()  # Pen up
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()  # Pen down
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[3][0], points[3][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


def get(p1, p2, V, H, show=False): # Vertical, Horizontal
    x1, y1 = p1
    x2, y2 = p2
    
    dx = x2 - x1
    dy = y2 - y1
    
    new_x = x1 + V/3 * dx
    new_y = y1 + H/3 * dy
    
    if show:
        print('NEW:', new_x, new_y)
        
    return new_x, new_y


def sierpinski(points, degree, myTurtle):
    
    colormap = ['blue', 'red', 'green', 'cyan', 'yellow',
                'violet', 'orange']
    
    # Draw a triangle based on the 3 points given
    drawTriangle(points, colormap[degree], myTurtle)

    if degree > 0:
        #print('--- 1 ---')
        #print(points)
        sierpinski([
                get(points[0], points[2], 0, 0),
                get(points[0], points[2], 0, 1),
                get(points[0], points[2], 1, 1),
                get(points[0], points[2], 1, 0)
               ], degree-1, myTurtle)

        #print('--- 2 ---')
        #print(points)
        sierpinski([
                get(points[0], points[2], 0, 1),
                get(points[0], points[2], 0, 2),
                get(points[0], points[2], 1, 2),
                get(points[0], points[2], 1, 1)
               ], degree-1, myTurtle)

        #print('--- 3 ---')
        #print(points)
        sierpinski([
                get(points[0], points[2], 0, 2),
                get(points[0], points[2], 0, 3),
                get(points[0], points[2], 1, 3),
                get(points[0], points[2], 1, 2)
               ], degree-1, myTurtle)

        #print('--- 4 ---')
        #print(points)
        sierpinski([
                get(points[0], points[2], 1, 2),
                get(points[0], points[2], 1, 3),
                get(points[0], points[2], 2, 3),
                get(points[0], points[2], 2, 2)
               ], degree-1, myTurtle)

        #print('--- 5 ---')
        #print(points)
        sierpinski([
                get(points[0], points[2], 2, 2),
                get(points[0], points[2], 2, 3),
                get(points[0], points[2], 3, 3),
                get(points[0], points[2], 3, 2)
               ], degree-1, myTurtle)

        #print('--- 6 ---')
        #print(points)
        sierpinski([
                get(points[0], points[2], 2, 1),
                get(points[0], points[2], 2, 2),
                get(points[0], points[2], 3, 2),
                get(points[0], points[2], 3, 1)
               ], degree-1, myTurtle)

        #print('--- 7 ---')
        #print(points)
        sierpinski([
                get(points[0], points[2], 2, 0),
                get(points[0], points[2], 2, 1),
                get(points[0], points[2], 3, 1),
                get(points[0], points[2], 3, 0)
               ], degree-1, myTurtle)

        #print('--- 8 ---')
        #print(points)
        sierpinski([
                get(points[0], points[2], 1, 0),
                get(points[0], points[2], 1, 1),
                get(points[0], points[2], 2, 1),
                get(points[0], points[2], 2, 0)
               ], degree-1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(0)  # adjust the drawing speed here
    myWin = turtle.Screen()
    
    size = 300
    # 3 points of the first triangle based on [x,y] coordinates
    myPoints = [[0, 0], [0, size], [size, size], [size, 0]]
    
    degree = 1  # Vary the degree of complexity here
    
    # first call of the recursive function
    sierpinski(myPoints, degree, myTurtle)

    myTurtle.hideturtle()  # hide the turtle cursor after drawing is completed
    myWin.exitonclick()  # Exit program when user click on window


main()
