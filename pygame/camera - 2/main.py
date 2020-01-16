#!/usr/bin/env python3

# date: 2020.01.16
# 

import pygame
import random

# --- constants ---

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = (RED, GREEN, BLUE)

TILE_SIZE = 50

# --- main ---

pygame.init()

# - window -
screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()

# - map - (with random rectangles)
fullmap = pygame.Surface((2000, 1000))
#for y in range(TILE_SIZE, 1000-TILE_SIZE, TILE_SIZE):
#    for x in range(TILE_SIZE, 2000-TILE_SIZE, TILE_SIZE):
for y in range(0, 1000, TILE_SIZE):
    for x in range(0, 2000, TILE_SIZE):
        pygame.draw.rect(fullmap, random.choice(COLORS), (x, y, TILE_SIZE, TILE_SIZE))
fullmap_rect = fullmap.get_rect()

# - icon(s) which not move -
icon = pygame.Surface((100, 100))
icon.fill((255,255,255))
icon_rect = icon.get_rect()
icon_rect.right = screen_rect.right - 10
icon_rect.bottom = screen_rect.bottom - 10

# - camera -
# `camera` is not `Surface` but only `Rect` with value/offset which I uses to cut map
camera = screen.get_rect()
             
# --- loop ---                         
running = True
while running:
    
    # - events -
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # - updates (without draws) -
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        camera.x -= 5
        if camera.left < fullmap_rect.left:
            camera.left = fullmap_rect.left
    if keys[pygame.K_RIGHT]:
        camera.x += 5
        if camera.right > fullmap_rect.right:
            camera.right = fullmap_rect.right
    if keys[pygame.K_UP]:
        camera.y -= 5
        if camera.top < fullmap_rect.top:
            camera.top = fullmap_rect.top
    if keys[pygame.K_DOWN]:
        camera.y += 5
        if camera.bottom > fullmap_rect.bottom:
            camera.bottom = fullmap_rect.bottom

    # - draws (without updates) -
    
    # moving map - using `camera` to copy part of `fullmap` to `screen`
    screen.blit(fullmap, (0,0), camera)
    
    # static icon(s)
    screen.blit(icon, icon_rect)
    
    pygame.display.update()
    
# --- end ---    
pygame.quit()
