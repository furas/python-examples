#!/usr/bin/env python3

import pygame

# --- constants ---

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

WIDTH  = 300
HEIGHT = 200

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()

# - frames/frames -

spritesheet = pygame.image.load('spritesheet008.jpg')

frames = []
frames.append(spritesheet.subsurface(pygame.Rect(  0,  75, 127, 56)))
frames.append(spritesheet.subsurface(pygame.Rect(127,  75, 127, 56)))
frames.append(spritesheet.subsurface(pygame.Rect(254,  75, 127, 56)))
frames.append(spritesheet.subsurface(pygame.Rect(381,  75, 127, 56)))
frames.append(spritesheet.subsurface(pygame.Rect(  0, 206, 127, 56)))
frames.append(spritesheet.subsurface(pygame.Rect(127, 206, 127, 56)))

frames_number = len(frames)
current_frame = 0

frame_rect = frames[0].get_rect(center=screen_rect.center)
move = 0

# - mainloop -

fps = pygame.time.Clock()

running = True

while running:

    # - events -
    
    for event in pygame.event.get():

        # - global events -
        
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # - player events -
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move += 1
            elif event.key == pygame.K_LEFT:
                move -= 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move -= 1
            elif event.key == pygame.K_LEFT:
                move += 1
                
    # - updates -

    current_frame = (current_frame + move) % frames_number
    frame_rect.x = (frame_rect.x + move*5) % WIDTH
    
    # - draws -

    screen.fill(WHITE)
    
    screen.blit(frames[current_frame], frame_rect)

    pygame.display.flip()

    fps.tick(10)
    
# - the end -

pygame.quit()   

