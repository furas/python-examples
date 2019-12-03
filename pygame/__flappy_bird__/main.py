#!/usr/bin/env python3 

# date: 2019.12.03
# https://stackoverflow.com/questions/59149195/how-to-resize-an-image-in-pygame-to-reach-the-top-bottom-of-screen

import pygame
import random

# --- constants --- (UPPER_CASE_NAMES)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# --- classes --- (CamelCaseNames)

# empty 

# --- main ---

gap_size = 200
ball_size = gap_size//4

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
screen_rect = screen.get_rect()

image = pygame.image.load("Obrazy/images/paddle.png").convert()
image = pygame.transform.scale(image, (50, SCREEN_HEIGHT))
image_rect = image.get_rect()

ball_rect = pygame.Rect((0, 0, ball_size, ball_size))
ball_rect.center = screen_rect.center

ball_speed = 5

# --- reset ---
pipes = []

# --- add ---
pipe1_rect = image_rect.copy()
pipe2_rect = image_rect.copy()

pipe1_rect.left = screen_rect.right # move to right of screen
pipe2_rect.left = screen_rect.right # move to right of screen

pipe1_rect.bottom = random.randint(50, SCREEN_HEIGHT-gap_size-50)
pipe2_rect.top = pipe1_rect.bottom + gap_size

pipes.append( (pipe1_rect, pipe2_rect) )
# ---

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_speed = -3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ball_speed = 4

    # --- changes/moves/updates ---

    ball_rect.y += ball_speed

    for pipe1_rect, pipe2_rect in pipes:
        pipe1_rect.x -= 1
        pipe2_rect.x -= 1

    for pipe1_rect, pipe2_rect in pipes:
        if pipe1_rect.colliderect(ball_rect) or pipe2_rect.colliderect(ball_rect):
            print('Game Over')
            # --- reset ---
            pipes = []

            # --- add ---
            pipe1_rect = image_rect.copy()
            pipe2_rect = image_rect.copy()
            
            pipe1_rect.left = screen_rect.right # move to right of screen
            pipe2_rect.left = screen_rect.right # move to right of screen
            
            pipe1_rect.bottom = random.randint(50, SCREEN_HEIGHT-gap_size-50)
            pipe2_rect.top = pipe1_rect.bottom + gap_size
            
            pipes.append( (pipe1_rect, pipe2_rect) )
            
    for pipe1_rect, pipe2_rect in pipes:
        if pipe1_rect.left == 0:
            print("POINT")
    
    if not screen_rect.contains(ball_rect):
        print('Game Over')
        # --- reset ---
        pipes = []

        # --- add ---
        pipe1_rect = image_rect.copy()
        pipe2_rect = image_rect.copy()
        
        pipe1_rect.left = screen_rect.right
        pipe2_rect.left = screen_rect.right
        
        pipe1_rect.bottom = random.randint(50, SCREEN_HEIGHT-gap_size-50)
        pipe2_rect.top = pipe1_rect.bottom + gap_size
        
        pipes.append( (pipe1_rect, pipe2_rect) )
        
    if pipes[-1][0].right < SCREEN_WIDTH - 200:
        # --- add ---
        pipe1_rect = image_rect.copy()
        pipe2_rect = image_rect.copy()
        
        pipe1_rect.left = screen_rect.right
        pipe2_rect.left = screen_rect.right
        
        pipe1_rect.bottom = random.randint(50, SCREEN_HEIGHT-gap_size-50)
        pipe2_rect.top = pipe1_rect.bottom + gap_size
        
        pipes.append((pipe1_rect, pipe2_rect))
        
    # --- draws ---

    screen.fill(BLACK)

    for pipe1_rect, pipe2_rect in pipes:
        screen.blit(image, pipe1_rect)
        screen.blit(image, pipe2_rect)

    pygame.draw.rect(screen, GREEN, ball_rect)

    pygame.display.flip()

    # --- FPS ---

    ms = clock.tick(FPS)
    #pygame.display.set_caption('{}ms'.format(ms)) # 40ms for 25FPS, 16ms for 60FPS
    fps = clock.get_fps()
    pygame.display.set_caption('FPS: {}'.format(fps))

# --- end ---

pygame.quit()
