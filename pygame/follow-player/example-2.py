#!/usr/bin/env python3

# ---------------------------------------------------------------------

__author__  = 'Bartlomiej "furas" Burek'
__email__   = 'furas@tlen.pl'
__webpage__ = 'http://blog.furas.pl'

# ---------------------------------------------------------------------

import pygame
import random

# === CONSTANS === (UPPER_CASE names)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

FPS = 30

# === CLASSES === (CamelCase names)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50,50))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        
        self.move_x = 0
        self.move_y = 0

        self.speed = 10
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_x -= self.speed
            elif event.key == pygame.K_RIGHT:
                self.move_x += self.speed
            elif event.key == pygame.K_UP:
                self.move_y -= self.speed
            elif event.key == pygame.K_DOWN:
                self.move_y += self.speed
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.move_x += self.speed
            elif event.key == pygame.K_RIGHT:
                self.move_x -= self.speed
            elif event.key == pygame.K_UP:
                self.move_y += self.speed
            elif event.key == pygame.K_DOWN:
                self.move_y -= self.speed
    
class Moster(pygame.sprite.Sprite):

    def __init__(self, speed=1, color=RED):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50,50))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center
        
        self.speed = speed

        self.all_speeds = [-self.speed, 0, self.speed]
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, player):

        move_x = random.choice(self.all_speeds)
        move_y = random.choice(self.all_speeds)

        self.rect.x += move_x
        self.rect.y += move_y
        

# === MAIN === (lower_case names)

# --- (global) variables --- 

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

player = Player()
monster1 = Moster(5, RED)
monster2 = Moster(2, BLUE)

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

        player.handle_event(event)
        
    # --- updates ---

    player.update()
    monster1.update(player)
    monster2.update(player)
    
    # --- draws ---
    
    screen.fill(BLACK)

    monster1.draw(screen)
    monster2.draw(screen)

    player.draw(screen)
    
    pygame.display.update()

    # --- FPS ---

    clock.tick(FPS)

# --- the end ---
    
pygame.quit()
