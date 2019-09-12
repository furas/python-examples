
# date: 2019.09.12
# https://stackoverflow.com/questions/57894963/bullet-pawn-in-pygame

import pygame
import math

# --- constants ---

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 15

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# --- classes ---

class Tank():

    def __init__(self, x, y):
        self.image_original = pygame.image.load('tank.png').convert_alpha()
        self.angle = 0
        self.dirty = False
        
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect(center=(x, y))

        self.turn_left = False
        self.turn_right = False
                
        self.distance = self.rect.height//2
        self.distance_vector = (0, self.rect.height//2)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        if self.turn_left:
            self.angle = (self.angle + 2) % 360
            self.dirty = True
        if self.turn_right:
            self.angle = (self.angle - 2) % 360
            self.dirty = True
            
        if self.dirty:
            self.dirty = False
            #print(self.angle)
            self.image = pygame.transform.rotate(self.image_original, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
          
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.turn_left = True
            elif event.key == pygame.K_RIGHT:
                self.turn_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.turn_left = False
            elif event.key == pygame.K_RIGHT:
                self.turn_right = False

    def get_barrel_end(self):
        rad = math.radians(self.angle)
        x = self.rect.centerx - math.sin(rad) * self.distance
        y = self.rect.centery - math.cos(rad) * self.distance
        return x, y
        
        
class Bullet():
    
    def __init__(self, x, y):
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        self.dirty = False
                
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self, x, y):
        self.rect.center = (x, y)            
          
    def handle_event(self, event):
        pass    
        
# --- main ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#, 32)
screen_rect = screen.get_rect()

tank = Tank(*screen_rect.center)
bullet = Bullet(*tank.get_barrel_end())

clock = pygame.time.Clock()
running = True
while running:

    # - events -
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        tank.handle_event(event)
        
    # - updates -
    
    tank.update()
    bullet.update(*tank.get_barrel_end())
    
    # - draws -
    
    screen.fill(WHITE)
    
    tank.draw(screen)
    bullet.draw(screen)
    
    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()        
    
    
    
