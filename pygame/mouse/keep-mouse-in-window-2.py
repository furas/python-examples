#!/usr/bin/env python

import pygame

''' 
it keeps mouse in window and it can move object with mouse
'''

import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

pos = pygame.Rect(0, 0, 100, 100)
pos.center = (400, 300)

clock = pygame.time.Clock()
running = True

pygame.event.set_grab(True)
pygame.mouse.set_pos(400, 300)
pygame.event.clear()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False
        if event.type == pygame.MOUSEMOTION:
            print(event.rel)
            pos.x -= event.rel[0]
            pos.y -= event.rel[1]

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), pos)
    pygame.display.flip()
    
    clock.tick(30)
    
pygame.quit()
