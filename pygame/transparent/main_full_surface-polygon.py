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
    image = pygame.surface.Surface((6*R, 6*R)) #.convert_alpha()
    
    # 100% transparent black background - it works
    #(black is default color for new surface - don't have to use fill((0,0,0)) )
    image.set_colorkey((0,0,0)) 
    
    # 0%-100% transparent all other colors
    image.set_alpha(alpha) 

    # it works
    pygame.draw.polygon(image, color, [(0,2*R), (6*R,2*R), (R, 6*R), (3*R, 0), (5*R, 6*R)])       
    
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

R = 50
ALPHA = 50

# --- init ---

pygame.init()

screen = pygame.display.set_mode((400, 400))
screen_rect = screen.get_rect()

# --- background ---

bg = create_background(screen_rect.size)
bg_rect = bg.get_rect()

# --- objects ---

poly = create_image((255, 0, 0), R, ALPHA)
poly_rect = poly.get_rect(center=screen_rect.center)

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
    poly.set_alpha(current_alpha)
    
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
    
    screen.blit(poly, poly_rect)
    
    pygame.display.flip()
    
    # --- FPS ---
    
    clock.tick(FPS)
       
# --- quit ---
    
pygame.quit()
