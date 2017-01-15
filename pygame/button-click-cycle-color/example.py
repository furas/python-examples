#!/usr/bin/env python

# http://stackoverflow.com/questions/33856739/how-to-cycle-3-images-on-a-rect-button

import pygame

# --- constants ---

WIDTH = 320
HEIGHT = 110

FPS = 5

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((300,200))
screen_rect = screen.get_rect()

# - objects -

# create three images/surfaces
images = [
    pygame.Surface((100,100)),
    pygame.Surface((100,100)),
    pygame.Surface((100,100)),
]

# set different colors
images[0].fill((255,0,0))
images[1].fill((0,255,0))
images[2].fill((0,0,255))

# get image rect and center it
images_rect = images[0].get_rect()
images_rect.center = screen_rect.center

# choose first image
index = 0

# - mainloop -

clock = pygame.time.Clock()
running = True

while running:

    # - events -

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # MOUSEBUTTONDOWN is created only once,
        # when button changes state from "not-pressed" to "pressed"
        # so it is better for this job then "pygame.mouse.get_pressed()"
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1 and images_rect.collidepoint(event.pos):
                # cycle index
                index = (index+1) % 3

    # - draws -

    screen.blit(images[index], images_rect)
    pygame.display.flip()

    # - FPS -

    clock.tick(FPS)

# - end -

pygame.quit()
