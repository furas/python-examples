
# author: https://blog.furas.pl
# date: 2020.07.16
# link: https://stackoverflow.com/questions/62940130/how-to-implement-a-scroll-view-in-pygame/

import pygame

# === CONSTANS === (UPPER_CASE names)

#BLACK = (  0,   0,   0)
#WHITE = (255, 255, 255)

#RED   = (255,   0,   0)
#GREEN = (  0, 255,   0)
#BLUE  = (  0,   0, 255)

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

image = pygame.image.load('image-800x600.jpg')
image_rect = image.get_rect()

# --- camera / offset ---

camera_rect = screen_rect.copy()

# --- mainloop ---

#button_pressed = False

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

        #elif event.type == pygame.MOUSEBUTTONDOWN:
        #    button_pressed = True
        #elif event.type == pygame.MOUSEBUTTONUP:
        #    button_pressed = False

        elif event.type == pygame.MOUSEMOTION:
            #if button_pressed:
    
                camera_rect.x += event.rel[0]
                # check left/right limit
                if camera_rect.left < image_rect.left:
                    camera_rect.left = image_rect.left
                if camera_rect.right > image_rect.right:
                    camera_rect.right = image_rect.right
    
                camera_rect.y += event.rel[1]
                # check up/down limit
                if camera_rect.top < image_rect.top:
                    camera_rect.top = image_rect.top
                if camera_rect.bottom > image_rect.bottom:
                    camera_rect.bottom = image_rect.bottom
                    
        # --- objects events ---

    # --- updates ---

        
    # --- draws ---
    
    #screen.fill(BLACK)

    # draw image
    screen.blit(image, (-camera_rect.x, -camera_rect.y))
    #screen.blit(image, camera_rect)

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---
    
pygame.quit()

