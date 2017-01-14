#!/usr/bin/env python3

#
# pygame (empty) template - by furas
#

import pygame

# === CONSTANS === (UPPER_CASE names)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

FPS = 60

# === CLASSES === (CamelCase names)

    # empty

# === FUNCTIONS === (lower_case names)

    # empty

# === MAIN === (lower_case names)

# --- (global) variables ---

# --- init ---

pygame.init()

# load image
background = pygame.image.load('background-1.png')
background_rect = background.get_rect()
w, h = background_rect.size

# set window
screen = pygame.display.set_mode(background_rect.size)
screen_rect = screen.get_rect()

# convert image
background = background.convert() # convert() has to be after set_mode()

# offset of moving image
offset = 0

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

    # --- updates ---

    offset += 1

    if offset >= w:
        offset = 0

    # --- draws ---

    screen.blit(background, (0,0), (offset, 0, w, h))
    screen.blit(background, (w-offset,0), (0, 0, offset, h))

    pygame.display.flip()

    # --- FPS ---

    clock.tick(FPS)

# --- the end ---

pygame.quit()
