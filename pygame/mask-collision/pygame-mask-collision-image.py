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

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

# === CLASSES === (CamelCase names)

class Image(pygame.sprite.Sprite):
    
    def __init__(self, screen_rect, image, angle=15, color=(255,0,0), rotate=5, resize=(100, 200)):
        super().__init__()

        self.angle = angle
        self.rotate = rotate

        self.original_image = pygame.image.load(image).convert()
        self.colorkey = self.original_image.get_at((0,0))
        #self.colorkey = (255, 212, 55)
        
        if resize:
            self.original_image = pygame.transform.scale(self.original_image, resize)
        
        self.change_angle = pygame.time.get_ticks()
            
        self.update()
        
    def update(self):
        if self.change_angle <= pygame.time.get_ticks():
            self.angle = (self.angle + self.rotate) % 360
            
            self.image = pygame.transform.rotate(self.original_image, self.angle).convert()
            self.image.set_colorkey(self.colorkey)

            self.rect = self.image.get_rect(center=screen_rect.center)
            self.mask = pygame.mask.from_surface(self.image)

            self.olist = self.mask.outline()

            #self.mask_image = pygame.Surface(self.rect.size, masks=self.mask) # ??? doesn't work as I expected

            if self.olist:
                pygame.draw.lines(self.image, (0, 0, 0), 3, self.olist)
        
            self.change_angle = pygame.time.get_ticks() + 50
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #screen.blit(self.mask_image, self.rect) # ??? doesn't work
            
# === FUNCTIONS === (lower_case names)

    # empty
    
# === MAIN === (lower_case names)

# --- (global) variables --- 

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

img1 = Image(screen_rect, 'player.png', 45, (0,255,0), 5)
img2 = Image(screen_rect, 'ball.png', 0, (0,255,255), 0, (50,50))

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
        elif event.type == pygame.MOUSEMOTION:
            img2.rect.center = event.pos
            
        # --- objects events ---

            # empty
        
    # --- updates ---

    img1.update()
    
    if pygame.sprite.collide_mask(img1, img2):
        bg_color = (255,200,200)
    else:
        bg_color = WHITE
    
    # --- draws ---
    
    screen.fill(bg_color)

    img1.draw(screen)
    img2.draw(screen)
    
    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---
    
pygame.quit()
