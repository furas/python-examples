#!/usr/bin/env python

# http://stackoverflow.com/questions/33856739/how-to-cycle-3-images-on-a-rect-button

import pygame

pygame.init()

screen = pygame.display.set_mode((300,200))

# three images 
images = [
    pygame.Surface((100,100)),    
    pygame.Surface((100,100)),    
    pygame.Surface((100,100)),    
]

images[0].fill((255,0,0))
images[1].fill((0,255,0))
images[2].fill((0,0,255))

images_rect = images[0].get_rect()

index = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and images_rect.collidepoint(event.pos):
                # cycle index
                index = (index+1) % 3
                
    screen.blit(images[index], images_rect)
    pygame.display.flip()
    
pygame.quit()
