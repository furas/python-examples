
#
# https://stackoverflow.com/a/48034477/1832058
# 

import pygame

pygame.init()

screen = pygame.display.set_mode((300, 200))

clock = pygame.time.Clock()
is_running = True

while is_running:

    changed = []

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False
        elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
            changed.append(event.key)

    print(changed)

    clock.tick(25)

pygame.quit()
