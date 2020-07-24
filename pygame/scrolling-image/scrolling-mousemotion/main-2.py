
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
SCREEN_HEIGHT = 600

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

percentage_x = 0
percentage_y = 0

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

        elif event.type == pygame.MOUSEMOTION:
            percentage_x = event.pos[0] / screen_rect.width
            camera_rect.x = percentage_x * (image_rect.width - screen_rect.width)

            #percentage_y = event.pos[1] / screen_rect.height
            #camera_rect.y = percentage_y * (image_rect.height - screen_rect.height)
                    
        # --- objects events ---
        
        # empty
        
    # --- updates ---

    # empty
        
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

