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

start_bottom = pygame.math.Vector2(screen_rect.centerx, screen_rect.bottom)
end_bottom = start_bottom

start_top = pygame.math.Vector2(screen_rect.centerx, screen_rect.top)
end_top = start_top

start_left = pygame.math.Vector2(screen_rect.left, screen_rect.centery)
end_left = start_left

start_right = pygame.math.Vector2(screen_rect.right, screen_rect.centery)
end_right = start_right

length = 100

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
            end_bottom = start_bottom + (mouse - start_bottom).normalize() * length
            end_top = start_top + (mouse - start_top).normalize() * length
            end_left = start_left + (mouse - start_left).normalize() * length
            end_right = start_right + (mouse - start_right).normalize() * length


        # --- objects events ---

            # empty

    # --- updates ---

        # empty

    # --- draws ---

    screen.fill(BLACK)

    pygame.draw.line(screen, RED, start_bottom, end_bottom)
    pygame.draw.line(screen, RED, start_top, end_top)
    pygame.draw.line(screen, RED, start_left, end_left)
    pygame.draw.line(screen, RED, start_right, end_right)

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()
