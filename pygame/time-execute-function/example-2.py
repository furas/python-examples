#!/usr/bin/env python3

import pygame

# --- constants ---

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((800, 600))

# - objects -

# current time
curr_time = pygame.time.get_ticks()

# first time check at once
green_start_showing = curr_time
green_end_showing   = curr_time + 1000
green_showing       = True
      
red_start_showing = curr_time
red_end_showing   = curr_time + 100
red_showing       = True

# other
rect = pygame.Rect(0, 0, 50, 50)

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
    
    curr_time = pygame.time.get_ticks()
    
    # execute function
    if not green_showing and curr_time >= green_start_showing:
        green_showing = True
        green_end_showing = curr_time + 1000
        
    if green_showing and curr_time >= green_end_showing:
        green_showing = False
        green_start_showing = curr_time + 1000

    if not red_showing and curr_time >= red_start_showing:
        red_showing = True
        red_end_showing = curr_time + 250
        
    if red_showing and curr_time >= red_end_showing:
        red_showing = False
        red_start_showing = curr_time + 250

    # other
    rect.center = pygame.mouse.get_pos()
    
    # - draws -

    screen.fill(BLACK)

    if green_showing:
        pygame.draw.rect(screen, GREEN, (0,0,100,100))
        
    if red_showing:
        pygame.draw.rect(screen, RED, (100,0,100,100))

    pygame.draw.rect(screen, WHITE, rect)

    pygame.display.flip()

    # - FPS -
    
    clock.tick(30)

# - end -

pygame.quit()
