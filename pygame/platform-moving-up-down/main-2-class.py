#!/usr/bin/env python3

# date: 2020.01.23
# https://stackoverflow.com/questions/59870590/collision-detection-ball-landing-on-platform

# Press SPACE to change player_gravity when it falls

import pygame

# --- constants --- (UPPER_CASE_NAMES)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 25 # for more than 220 it has no time to update screen

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- classes --- (CamelCaseNames)

class Player():

    def __init__(self):
        self.rect = pygame.Rect(0,0,50,50)
        self.color = (0,255,0)
        self.rect.centerx = screen_rect.centerx
        self.rect.bottom = screen_rect.bottom-25
        self.gravity = 5 # try 5
        self.speed_y = 0
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)    

    def update(self):
        if self.speed_y < 0:
            self.speed_y += 1
        
        # move player down - to move down with platform
        self.rect.y += self.gravity + self.speed_y

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.speed_y = -20
                        
class Platform():

    def __init__(self, x, y, w, h, min_y, max_y):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255,0,0)
        self.min_y = 100
        self.max_y = 600
        self.speed = 5
        self.direction = 'top'
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)    

    def update(self):
        self.rect.y -= self.speed
        if self.direction == 'top':
            if self.rect.top <= self.min_y:
                self.direction = 'bottom'
                self.speed = -self.speed
        else:
            if self.rect.bottom >= self.max_y:
                self.direction = 'top'
                self.speed = -self.speed
        
# --- functions --- (lower_case_names)

# --- main ---

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
screen_rect = screen.get_rect()

player = Player()
platforms = [
    Platform(  0, 500-25, 200, 25, 100, 600),
    Platform(300, 600-25, 200, 25, 100, 600),
    Platform(600, 400-25, 200, 25, 100, 600),
]    

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

        player.handle_event(event)
        
    # --- changes/moves/updates ---

    player.update()
    
    for p in platforms:
        p.update()

    # move player up with platform    
    for p in platforms:
        if player.rect.colliderect(p.rect):
            player.rect.bottom = p.rect.top

    # --- draws ---

    screen.fill(BLACK)

    player.draw(screen)
    
    for p in platforms:
        p.draw(screen)
    
    pygame.display.flip()

    # --- FPS ---

    ms = clock.tick(FPS)
    
# --- end ---

pygame.quit()
 
