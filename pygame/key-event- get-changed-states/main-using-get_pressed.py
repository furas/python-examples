#!/usr/bin/env python3

#
# https://stackoverflow.com/a/48034477/1832058
# 

import pygame

pygame.init()

screen = pygame.display.set_mode((300, 200))

pressed = pygame.key.get_pressed()

clock = pygame.time.Clock()
is_running = True

while is_running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    last_pressed = pressed
    pressed = pygame.key.get_pressed()
    
    # --- get only keys which changed state ---
    
    changed = [idx for idx in range(len(pressed)) if pressed[idx] != last_pressed[idx]]
    print(changed)
    # or
    changed = [idx for idx, (a, b) in enumerate(zip(last_pressed, pressed)) if a != b]
    print(changed)

    # --- True/False for all keys ---
    
    changed = [pressed[idx] != last_pressed[idx] for idx in range(len(pressed))]
    print(changed)
    # or
    changed = [a != b for a, b in zip(last_pressed, pressed)]
    print(changed)

    # ---
    
    clock.tick(25)

pygame.quit()
