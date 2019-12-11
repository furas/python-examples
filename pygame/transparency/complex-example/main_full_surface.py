#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Created: 2017.10.31

author: furas@tlen.pl

"full surface" transparency - set_alpha()
plus 
"key color" transparency - set_colorkey()

It uses only (R,G,B) colors, not (R,G,B,A)
"""

import pygame

#----------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------

def create_image(color, R, alpha):

    # create surface for circle
    image = pygame.surface.Surface((2*R, 2*R)) #.convert_alpha()
    
    # 100% transparent black background - ALPHA=0 doesn't work
    #image.fill((0,0,0,0)) 

    # 100% transparent black background - it works
    #(black is default color for new surface - don't have to use fill((0,0,0)) )
    image.set_colorkey((0,0,0)) 
    
    # 0%-100% transparent all other colors
    image.set_alpha(alpha) 

    # it works
    pygame.draw.circle(image, color, (R, R), R)       
    pygame.draw.circle(image, (0,0,0), (R, R), R//3)  # hole in the middle - black = 100% transparent

    # it doesn't work
    #pygame.draw.circle(image, (*color, 20),  (R, R), R)      # points with ALPHA=20
    #pygame.draw.circle(image, (*color, 40),  (R, R), 3*R//4) # points with ALPHA=40
    #pygame.draw.circle(image, (*color, 60),  (R, R), 2*R//4) # points with ALPHA=60 
    #pygame.draw.circle(image, (*color, 255), (R, R), 1*R//4) # points with ALPHA=255 
    #pygame.draw.circle(image, (*color, 0),   (R, R), 1*R//8) # hole in the middle - ALPHA=0
    
    return image

def create_background(size):
    BG_COLOR_1 = (50, 50, 50)
    BG_COLOR_2 = (100, 100, 100)
    RECT_SIZE = 25

    image = pygame.surface.Surface(size)
    image.fill(BG_COLOR_1)
    
    for y in range(0, 400, RECT_SIZE):
        start = y % (RECT_SIZE*2)
        for x in range(start, 400, (RECT_SIZE*2)):
            pygame.draw.rect(image, BG_COLOR_2, (x, y, RECT_SIZE, RECT_SIZE), 0)

    return image

#----------------------------------------------------------------------
# MAIN
#----------------------------------------------------------------------

FPS = 25

R = 100
ALPHA = 50

# --- init ---

pygame.init()

screen = pygame.display.set_mode((400, 400))
screen_rect = screen.get_rect()

# --- background ---

bg = create_background(screen_rect.size)
bg_rect = bg.get_rect()

# --- objects ---

s1 = create_image((255, 0, 0), R, ALPHA)
s1_rect = s1.get_rect(center=screen_rect.center).move(-R//2, -R//2)

s2 = create_image((0, 255, 0), R, ALPHA)
s2_rect = s2.get_rect(center=screen_rect.center).move(R//2, -R//2)

s3 = create_image((0, 0, 255), R, ALPHA)
s3_rect = s3.get_rect(center=screen_rect.center).move(0, R//2)


current_alpha = 0
step_alpha = 5

# --- mainloop ---

clock = pygame.time.Clock()
running = True

while running:
    
    # --- events ---
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # --- updates ---
    
    # set new transparency - it works
    s1.set_alpha(current_alpha)
    s2.set_alpha(current_alpha)
    s3.set_alpha(current_alpha)
    
    # change alpha step 
    current_alpha += step_alpha

    if current_alpha >= 255:
        current_alpha = 255
        step_alpha = -step_alpha # change direction
    elif current_alpha <= 0:
        current_alpha = 0
        step_alpha = -step_alpha # change direction
        
    # --- draws ---
    
    screen.blit(bg, bg_rect)
    
    screen.blit(s1, s1_rect)
    screen.blit(s2, s2_rect)
    screen.blit(s3, s3_rect)
    
    pygame.display.flip()
    
    # --- FPS ---
    
    clock.tick(FPS)
       
# --- quit ---
    
pygame.quit()
