#!/usr/bin/env python3

import pygame

# --- constants ---

WIDTH = 800
HEIGHT = 800

FPS = 25

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

BULLET_SPEED = 5

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
center = pygame.math.Vector2(screen.get_rect().center)

shot = False

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type== pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                shot = event.pos

        elif event.type== pygame.MOUSEBUTTONUP:
            if event.button == 1:
                shot = None

        elif event.type== pygame.MOUSEMOTION:
            if shot:
                shot = event.pos


    # create new bullet
    if shot:
        # get vector from center to mouse position
        vector = shot - center
        # `center` is `Vector2` so `vector` will be `Vector2` too
        #print(type(vector))

        # normalize
        normal = vector.normalize()

        # create speed vector
        speed = normal * BULLET_SPEED

        # move object (first move 15 times bigger then next moves )
        pos = center# + (speed * 15)
        pos = pygame.math.Vector2(center)

        previous = pygame.math.Vector2(center)

        #pygame.draw.line(screen, (255,150,100), (pos.x, pos.y), (center.x, center.y))
        pygame.draw.line(screen, (255,150,100), pos, previous)

        # remeber position and speed as one object
        bullets.append( [pos, speed, previous] )

    # - updates (without draws) -

    new_bullets = []

    for pos, speed, previous in bullets:
        #previous.x = pos.x
        #previous.y = pos.y

        # move
        pos += speed

        if screen_rect.collidepoint(pos):
            new_bullets.append( [pos, speed, previous] )

    bullets = new_bullets

    # - draws -

    screen.fill(BLACK)

    for pos, speed, previous in bullets:
        # draw
        #pygame.draw.line(screen, (255,150,100), pos, previous)
        pygame.draw.rect(screen, WHITE, (pos.x, pos.y, 2, 2))

    pygame.display.update()

    # - speed -

    clock.tick(FPS)

# - end -

pygame.quit()
quit()

