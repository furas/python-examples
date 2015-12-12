#!/usr/bin/env python

# http://stackoverflow.com/questions/33856739/how-to-cycle-3-images-on-a-rect-button

import pygame

class Button(object):

    def __init__(self, position, size):
        self._images = [
            pygame.Surface(size),    
            pygame.Surface(size),    
            pygame.Surface(size),    
        ]

        self._images[0].fill((255,0,0))
        self._images[1].fill((0,255,0))
        self._images[2].fill((0,0,255))

        self._rect = pygame.Rect(position, size)

        self._index = 0

    def draw(self, screen):
        screen.blit(self._images[self._index], self._rect)

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self._rect.collidepoint(event.pos):
                self._index = (self._index+1) % 3
        
        
pygame.init()

screen = pygame.display.set_mode((320,110))

button1 = Button((5, 5), (100, 100))
button2 = Button((110, 5), (100, 100))
button3 = Button((215, 5), (100, 100))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        button1.event_handler(event)
        button2.event_handler(event)
        button3.event_handler(event)
                    
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()
