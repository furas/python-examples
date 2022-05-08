# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.04.14

import pygame
import random

# --- constants --- (UPPER_CASE_NAMES)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)

FPS = 25 # for more than 220 it has no time to update screen

# --- main ---

pygame.init()
pygame.scrap.init()
pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)
#pygame.scrap.set_mode(pygame.SCRAP_SELECTION)

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

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
            
            elif event.key == pygame.K_v and event.mod & pygame.KMOD_CTRL:
                print('Clipboard:', pygame.scrap.get(pygame.SCRAP_TEXT))
                print('Clipboard:', pygame.scrap.get("text/plain;charset=utf-8").decode())
                
                for t in pygame.scrap.get_types():
                    r = pygame.scrap.get(t)
                    print('>', t, r)
                    
    # --- draws ---

    screen.fill(BLACK)
    
    pygame.display.flip()

    # --- FPS ---

    ms = clock.tick(FPS)
    
# --- end ---

pygame.quit()
 
