#!/usr/bin/env python3

'''
with line which shows way
'''

import pygame

# --- constants ---

WIDTH = 800
HEIGHT = 800

FPS = 25

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

BULLET_SPEED = 15

# --- classes ---

#empty

# --- functions ---

#empty

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()

# - objects -

bullets = []

# center of screen as Vector2
#center = pygame.math.Vector2(WIDTH//2, HEIGHT//2)
center = pygame.math.Vector2(screen_rect.center)

# - mainloop -

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type== pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                # get vector from center to mouse position
                vector = event.pos - center
                # `center` is `Vector2` so `vector` will be `Vector2` too
                #print(type(vector))

                # normalize
                normal = vector.normalize()
                # create speed vector
                speed = normal * BULLET_SPEED

                # move object (first move 5 times bigger then next moves )
                #pos = center + (speed * 15)
                #pos = center + speed
                pos = pygame.math.Vector2(center)

                previous = pygame.math.Vector2(center)

                # remeber position and speed as one object
                bullets.append( [pos, speed, previous] )

    # - updates (without draws)-

    existing_bullets = []

    for pos, speed, previous in bullets:
        # copy from `pos` to `previous`
        # can't do `previous = pos`
        previous.x = pos.x
        previous.y = pos.y

        # move
        pos += speed

        # check if bullet still on screen
        if screen_rect.collidepoint(pos):
            existing_bullets.append( [pos, speed, previous] )

    bullets = existing_bullets

    # - draws (without updates)-

    screen.fill(BLACK)

    for pos, speed, previous in bullets:
        # draw
        pygame.draw.line(screen, GREEN, pos, previous)
        pygame.draw.rect(screen, WHITE, (pos.x-3, pos.y-3, 6, 6))

    pygame.display.update()

    # - speed -

    clock.tick(FPS)

# - end -


