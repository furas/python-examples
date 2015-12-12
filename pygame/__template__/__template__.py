#!/usr/bin/env python

import pygame

# === CONSTANTS ===

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

WIDTH  = 600
HEIGHT = 400

# === CLASSES ===

    # empty
    
# === FUNCTIONS ===

    # empty
    
# === MAIN ===

# - init -

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# - objects -

#img = pygame.Surface((50,50))
#img.fill(GREEN)
#img_rect = img.get_rect()
#img_rect.center = screen.get_rect().center

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

    # - updates -

        # empty

    # - draws -
    
    screen.fill(BLACK)

    # screen.blit(img, img_rect)    
    
    pygame.display.flip()

    # - FPS -

    clock.tick(25)

# - the end -
    
pygame.quit()
