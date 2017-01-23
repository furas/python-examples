#!/usr/bin/env python3

'''
angle between "line from A to B" and "horizontal line"
'''

import math
import pygame

data = [
    [(5, 2), (4, 6)],   # 104.03624346792648
    [(0, 0), (14, 14)], #  45.0
    [(0, 0), (0, 14)],  #  90.0
    [(0, 0), (0, -14)], # -90.0
    [(0, 0), (14, 0)],  #   0.0
    [(0, 0), (-14, 0)], # 180.0
    [(0, 0), (2, 1.31545)], # 33.333
]

for (ax, ay), (bx, by) in data:

    print("  Math:", math.degrees(math.atan2(by - ay, bx - ax)))

    #a = pygame.math.Vector2( (ax, ay) )
    #b = pygame.math.Vector2( (bx, by) )
    # or
    a = pygame.math.Vector2(ax, ay)
    b = pygame.math.Vector2(bx, by)

    zero = pygame.math.Vector2()

    print('PyGame:', zero.angle_to(b-a))

    #a = pygame.math.Vector2( pygame.mouse.get_pos() )
    #b = pygame.math.Vector2( player.rect.center )

