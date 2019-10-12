#!/usr/bin/env python3

# date: 2019.10.10
# https://stackoverflow.com/questions/58331808/pygame-set-at-for-pygame-surface-objects-doesnt-apply-to-tuple-object

# surface = pygame.Surface((800,600))
# surface.set_at((i, j), (255,255,255))
# screen.blit(surface, (0, 0))
# # or
# screen = pygame.display.set_mode((800,600))
# screen.set_at((i, j), (255,255,255))
# # or
# image = pygame.image.load('image.png')
# image.set_at((i, j), (255,255,255))
# screen.blit(image, (0, 0))
# # or
# font = pygame.font.SysFont(None, 20)
# text = font.render("Hello World", True, (255,255,255))
# text.set_at((i, j), (255,255,255))
# screen.blit(text, (0, 0))

import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

#WHITE = pygame.color.Color('white')
WHITE = (255,255,255)

for x in range(100):
    for y in range(100):
        screen.set_at((350+x, 250+y), WHITE)

        
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
