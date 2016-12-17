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

BOX = 30 # arrow size

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

# --- camera / offset ---

camera_rect = screen_rect.copy()

# place for arrows/scrolls
camera_rect.width -= BOX
camera_rect.height -= BOX

camera_move_x = 0
camera_move_y = 0

# --- arrows ---

arrow_left = pygame.Rect(screen_rect.left, screen_rect.bottom-BOX, BOX, BOX)
arrow_right = pygame.Rect(screen_rect.right-(2*BOX), screen_rect.bottom-BOX, BOX, BOX)

arrow_up = pygame.Rect(screen_rect.right-BOX, 0, BOX, BOX)
arrow_down = pygame.Rect(screen_rect.right-BOX, screen_rect.bottom-(2*BOX), BOX, BOX)

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

        # --- objects events ---

    # check mouse click in arrows
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if arrow_left.collidepoint(pos):
            camera_move_x = -15
        elif arrow_right.collidepoint(pos):
            camera_move_x = +15
        else:
            camera_move_x = 0

        if arrow_up.collidepoint(pos):
            camera_move_y = -15
        elif arrow_down.collidepoint(pos):
            camera_move_y = +15
        else:
            camera_move_y = 0
    else:
        camera_move_x = 0
        camera_move_y = 0
        
    # --- updates ---

    # move image

    if camera_move_x != 0:
        camera_rect.x += camera_move_x
        # check left/right limit
        if camera_rect.left < image_rect.left:
            camera_rect.left = image_rect.left
        if camera_rect.right > image_rect.right:
            camera_rect.right = image_rect.right

    if camera_move_y != 0:
        camera_rect.y += camera_move_y
        # check up/down limit
        if camera_rect.top < image_rect.top:
            camera_rect.top = image_rect.top
        if camera_rect.bottom > image_rect.bottom:
            camera_rect.bottom = image_rect.bottom
        
    # --- draws ---
    
    screen.fill(BLACK)

    #screen.blit(image, screen_rect, camera_rect)

    # draw image
    pos = screen_rect.move(-camera_rect.x, -camera_rect.y)
    screen.blit(image, pos)

    # draw arrows
    pygame.draw.rect(screen, (255,0,0), arrow_left)
    pygame.draw.rect(screen, (255,0,0), arrow_right)
    pygame.draw.rect(screen, (255,0,0), arrow_up)
    pygame.draw.rect(screen, (255,0,0), arrow_down)
    
    # draw scrollbars
    pygame.draw.rect(screen, (128,128,128), (BOX,screen_rect.bottom-BOX,screen_rect.width-(3*BOX), BOX))
    pygame.draw.rect(screen, (128,128,128), (screen_rect.right-BOX,BOX,BOX, screen_rect.height-(3*BOX)))

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---
    
pygame.quit()
