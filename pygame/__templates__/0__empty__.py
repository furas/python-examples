#!/usr/bin/env python3

#
# pygame (empty) template - by furas
#

# ---------------------------------------------------------------------

__author__  = 'Bartlomiej "furas" Burek'
__webpage__ = 'http://blog.furas.pl'

# ---------------------------------------------------------------------

import pygame

# === CONSTANS === (UPPER_CASE names)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

# === CLASSES === (CamelCase names)

    # empty
    
# === FUNCTIONS === (lower_case names)

    # empty
    
# === MAIN === (lower_case names)

# --- (global) variables --- 

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

    # empty

# --- mainloop ---

clock = pygame.time.Clock()
is_running = True

while is_running:

    # --- events ---
    
    for event in pygame.event.get():

        # --- global events ---
        
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

        # --- objects events ---

            # empty
        
    # --- updates ---

        # empty
    
    # --- draws ---
    
    screen.fill(BLACK)

        # empty
    
    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---
    
pygame.quit()
