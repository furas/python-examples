#!/usr/bin/env python3

# http://stackoverflow.com/questions/33856739/how-to-cycle-3-images-on-a-rect-button

import pygame

# --- constants ---

WIDTH = 320
HEIGHT = 110

FPS = 5

# --- class ---

class Button(object):

    def __init__(self, position, size):

        # create 3 images
        self.images = [
            pygame.Surface(size),
            pygame.Surface(size),
            pygame.Surface(size),
        ]

        # fill images with color - red, gree, blue
        self.images[0].fill((255,0,0))
        self.images[1].fill((0,255,0))
        self.images[2].fill((0,0,255))

        # get image size and position
        self.rect = pygame.Rect(position, size)

        # select first image
        self.index = 0

    def draw(self, screen):

        # draw selected image
        screen.blit(self.images[self.index], self.rect)

    def event_handler(self, event):

        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.index = (self.index+1) % 3

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()

# - objects -

# create buttons
button1 = Button((5, 5), (100, 100))
button2 = Button((110, 5), (100, 100))
button3 = Button((215, 5), (100, 100))

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

        button1.event_handler(event)
        button2.event_handler(event)
        button3.event_handler(event)

    # - draws -

    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)

    pygame.display.flip()

    # - FPS -

    clock.tick(FPS)

# - end -

pygame.quit()
