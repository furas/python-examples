#!/usr/bin/env python3

import pygame

# === CONSTANS === (UPPER_CASE names)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

# === MAIN === (lower_case names)

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

start = pygame.math.Vector2(screen_rect.centerx, screen_rect.bottom)
end = start
length = 150

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
        elif event.type == pygame.MOUSEMOTION:
            #mouse = pygame.math.Vector2(pygame.mouse.get_pos()) # edited
            mouse = pygame.mouse.get_pos()
            end = start + (mouse - start).normalize() * length

        # --- objects events ---

            # empty

    # --- updates ---

        # empty

    # --- draws ---

    screen.fill(BLACK)

    pygame.draw.line(screen, RED, start, end)

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()
