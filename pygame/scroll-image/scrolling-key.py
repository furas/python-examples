#!/usr/bin/env python3

#
# pygame (empty) template - by furas
#

# ---------------------------------------------------------------------

import pygame

# === CONSTANS === (UPPER_CASE names)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 400
SCREEN_HEIGHT = 300

# === CLASSES === (CamelCase names)

    # empty
    
# === FUNCTIONS === (lower_case names)

    # empty
    
# === MAIN === (lower_case names)

# --- (global) variables --- 

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

image = pygame.image.load('background-1.png')
image_rect = image.get_rect()

camera_rect = screen_rect.copy()
camera_move_x = 0
camera_move_y = 0

arrow_left = pygame.Rect(screen_rect.left, screen_rect.bottom-30, 30, 30)
arrow_right = pygame.Rect(screen_rect.right-30, screen_rect.bottom-60, 30, 30)

arrow_up = pygame.Rect(screen_rect.left, 0, 30, 30)
arrow_down = pygame.Rect(screen_rect.right-30, 0, 30, 30)
# --- mainloop ---

clock = pygame.time.Clock()
is_running = True

while is_running:

    # --- events ---
    
    for event in pygame.event.get():

        # --- global events ---
        
        if event.type == pygame.QUIT:
            is_running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
                
            elif event.key == pygame.K_LEFT:
                camera_move_x -= 5
            elif event.key == pygame.K_RIGHT:
                camera_move_x += 5

            elif event.key == pygame.K_UP:
                camera_move_y -= 5
            elif event.key == pygame.K_DOWN:
                camera_move_y += 5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                camera_move_x += 5
            elif event.key == pygame.K_RIGHT:
                camera_move_x -= 5
            elif event.key == pygame.K_UP:
                camera_move_y += 5
            elif event.key == pygame.K_DOWN:
                camera_move_y -= 5


        # --- objects events ---


    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if arrow_left.collidepoint(pos):
            camera_move_x = -5
        elif arrow_right.collidepoint(pos):
            camera_move_x = +5
        else:
            camera_move_x = 0
        
    # --- updates ---

    camera_rect.x += camera_move_x

    if camera_rect.left < image_rect.left:
        camera_rect.left = image_rect.left
    if camera_rect.right > image_rect.right:
        camera_rect.right = image_rect.right

    camera_rect.y += camera_move_y

    if camera_rect.top < image_rect.top:
        camera_rect.top = image_rect.top
    if camera_rect.bottom > image_rect.bottom:
        camera_rect.bottom = image_rect.bottom
        
    # --- draws ---
    
    screen.fill(BLACK)

    #screen.blit(image, screen_rect, camera_rect)
    pos = screen_rect.move(-camera_rect.x, -camera_rect.y)
    screen.blit(image, pos)

    pygame.draw.rect(screen, (255,0,0), arrow_left)
    pygame.draw.rect(screen, (255,0,0), arrow_right)

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---
    
pygame.quit()
