#!/usr/bin/env python3

# date: 2020.01.23
# https://stackoverflow.com/questions/59870590/collision-detection-ball-landing-on-platform

# Press SPACE to change player_gravity when it falls

import pygame

# --- constants --- (UPPER_CASE_NAMES)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 25 # for more than 220 it has no time to update screen

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- classes --- (CamelCaseNames)

# --- functions --- (lower_case_names)

# --- main ---

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
screen_rect = screen.get_rect()

player_rect = pygame.Rect(0,0,50,50)
player_color = (0,255,0)
player_rect.centerx = screen_rect.centerx
player_rect.bottom = screen_rect.bottom-25
player_gravity = 3 # try 5

platform_rect = pygame.Rect(0,0,200,25)
platform_color = (255,0,0)
platform_rect.centerx = screen_rect.centerx
platform_rect.bottom = screen_rect.bottom
platform_direction = 'top'
platform_speed = 5

# --- mainloop ---

clock = pygame.time.Clock()

running = True
while running:

    # --- events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                if player_gravity == 3:
                    player_gravity = 10
                else:
                    player_gravity = 3

    # --- changes/moves/updates ---

    if platform_direction == 'top':
        platform_rect.y -= platform_speed
        if platform_rect.top <= 100:
            platform_direction = 'bottom'
    else:
        platform_rect.y += platform_speed
        if platform_rect.bottom >= 600:
            platform_direction = 'top'
    
    player_rect.y += player_gravity 
    
    if player_rect.colliderect(platform_rect):
        player_rect.bottom = platform_rect.top

    # --- draws ---

    screen.fill(BLACK)

    pygame.draw.rect(screen, player_color, player_rect)    
    pygame.draw.rect(screen, platform_color, platform_rect)    
    
    pygame.display.flip()

    # --- FPS ---

    ms = clock.tick(FPS)
    
# --- end ---

pygame.quit()
 
