import math

def move(x1, y1, x2, y2, speed):

    # distance
    dx = x2 - x1
    dy = y2 - y1

    # angle
    angle = math.atan2(dx, dy)
    #print(math.degrees(angle))

    # 
    cx = speed * math.sin(angle)
    cy = speed * math.cos(angle)
    #print(cx, cy)

    # if distance is smaller then `cx/cy`
    # then you have to stop in target.

    if abs(cx) < abs(dx) or abs(cy) < abs(dy):
        # move bullet to new position
        x1 += cx
        y1 += cy
        in_target = False
    else:
        # move bullet to target
        x1 = x2
        y1 = y2
        in_target = True

    return x1, y1, in_target

#--- 

speed = 10

# bullet position
x1 = 10
y1 = 0

# taget possition
x2 = -130
y2 = 30

print('x: {:6.02f} | y: {:6.02f}'.format(x1, y1))

in_target = False

while not in_target and :
    x1, y1, in_target = move(x1, y1, x2, y2, speed)
    print('x: {:6.02f} | y: {:6.02f}'.format(x1, y1))
