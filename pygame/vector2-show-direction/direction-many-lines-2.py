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

length = 100

all_starts = []
all_ends = []
for offset in range(-250, 251, 50):
    
    all_starts.append(start)
    end = pygame.math.Vector2(screen_rect.centerx+offset, screen_rect.bottom-length)
    all_ends.append(end)

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
            
            all_ends = []
            for start in all_starts:
                end = start + (mouse - start).normalize() * length
                all_ends.append(end)

        # --- objects events ---

            # empty

    # --- updates ---

        # empty

    # --- draws ---

    screen.fill(BLACK)

    for start, end in zip(all_starts, all_ends):
        pygame.draw.line(screen, RED, start, end)
    
    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()
