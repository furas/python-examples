#!/usr/bin/env python3 

# date: 2019.12.11
# https://stackoverflow.com/questions/59293057/how-to-make-transparent-pygame-draw-circle/

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))#, depth=32)

surface1 = screen.convert_alpha()
surface1.fill([0,0,0,0])
pygame.draw.circle(surface1, (255, 0, 0, 128), (325, 250), 100)

surface2 = screen.convert_alpha()
surface2.fill([0,0,0,0])
pygame.draw.circle(surface2, (0, 255, 0, 128), (475, 250), 100)

surface3 = screen.convert_alpha()
surface3.fill([0,0,0,0])
pygame.draw.circle(surface3, (0, 0, 255, 128), (400, 350), 100)

screen.fill([255,255,255]) # white background
screen.blit(surface1, (0,0))
screen.blit(surface2, (0,0))
screen.blit(surface3, (0,0))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()    
