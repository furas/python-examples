#!/usr/bin/env python

# date: 2019.07.11
# https://stackoverflow.com/questions/56984542/is-there-an-effiecient-way-of-making-a-function-to-drag-and-drop-multiple-pngs

# It drags two images at the same time, You can click in any place.

import pygame

# --- constants ---

RED = (213, 43, 67)

# --- main ---

pygame.init()
screen = pygame.display.set_mode((800,600))

chew1 = pygame.image.load("hal_9000.jpg")
chew1_rect = chew1.get_rect(x=400, y=400)

chew2 = pygame.image.load("hal_9000.jpg") # use different image
chew2_rect = chew1.get_rect(x=200, y=200)

drag = 0

# --- mainloop ---

clock = pygame.time.Clock()
game_exit = False

while not game_exit:

    # - events -
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drag = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            drag = 0
        elif event.type == pygame.MOUSEMOTION:
            if drag:
                chew1_rect.move_ip(event.rel)
                chew2_rect.move_ip(event.rel)

    # - draws -            
    screen.fill(RED)
    screen.blit(chew1, chew1_rect)
    screen.blit(chew2, chew2_rect)
    pygame.display.update()

    # - FPS -
    clock.tick(30)

# --- end ---

pygame.quit()
