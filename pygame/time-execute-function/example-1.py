#!/usr/bin/env python3

import pygame

# --- constants ---

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((800, 600))

# - objects -

# current time
curr_time = pygame.time.get_ticks()

# first time check at once
check_time = curr_time

# other
rect = pygame.Rect(0, 0, 100, 100)

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
    if curr_time >= check_time:
        print('time to do it')
        # check again after 1000ms (1s)
        check_time = curr_time + 1000

    # other
    rect.center = pygame.mouse.get_pos()
    
    # - draws -

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, rect)
    pygame.display.flip()

    # - FPS -
    
    clock.tick(30)

# - end -

pygame.quit()
