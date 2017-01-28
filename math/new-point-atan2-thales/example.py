import math

'''
Calculate new point on the same line as P1 and P2
'''

def new_coordinates_1(point_one, point_two):

    dx = (point_two[0] - point_one[0])
    dy = (point_two[1] - point_one[1])

    distance = math.sqrt(dx**2 + dy**2)

    angle = math.atan2(dy, dx)

    a = math.cos(angle) * (distance/0.5)
    b = math.sin(angle) * (distance/0.5)

    x_a = point_one[0] - a
    y_b = point_one[1] - b

    return (round(x_a), round(y_b))

def new_coordinates_2(point_one, point_two):

    '''
    Based on "The intercept theorem", also known as "Thales' theorem"
    https://en.wikipedia.org/wiki/Intercept_theorem
    '''

    dx = (point_two[0] - point_one[0])
    dy = (point_two[1] - point_one[1])

    x_a = point_one[0] - dx/0.5
    y_b = point_one[1] - dy/0.5

    return (round(x_a), round(y_b))

# --- test ---

data = [
    ((400,400), (600,200)),
    ((400,400), (600,100)),
    ((400,400), (600,400)),
    ((400,400), (400,100)),
    ((400,400), (200,100)),
    ((400,400), (200,500)),
]

for p1, p2 in data:
    print(p1, p2)
    print("#1 New points", new_coordinates_1(p1, p2))
    print("#2 New points", new_coordinates_2(p1, p2))
    print('---')
