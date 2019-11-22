#!/usr/bin/env python3

# date: 2019.11.07
# https://stackoverflow.com/questions/58750187/move-an-object-on-its-own-with-pygame/58751128

import pygame

# --- constans ---

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 600
FPS = 20
SPEED = 5

# --- classes ---

class Colors:
    blue  = (000, 000, 255)
    black = (000, 000, 000)
    red   = (255, 000, 000)

class Circle:

    def __init__(self, x, y, size=50, thick=5, color=Colors.blue, speed=SPEED):

        self.size = size
        self.thick = thick
        self.color = color

        self.rect = pygame.Rect(0, 0, 2*size, 2*size)
        self.rect.centerx = x
        self.rect.centery = y
        if speed >= 0:
            self.direction = 'up'
        else:
            self.direction = 'down'

        self.speed = speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.size, self.thick)

    def update(self):
        self.rect.y -= self.speed

        if self.rect.top <= 0 and self.direction == 'up':
            self.direction = 'down'
            self.speed = -self.speed

        if self.rect.bottom >= screen_rect.bottom and self.direction == 'down':
            self.direction = 'up'
            self.speed = -self.speed

# --- main ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

circles = [
    Circle(screen_rect.centerx, screen_rect.centery),
    Circle(screen_rect.centerx, screen_rect.centery, speed=-SPEED, color=Colors.red)
]

clock = pygame.time.Clock()

game_over = False

while not game_over:

    # --- events ----

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- updates --- (without draws)    

    for item in circles:
        item.update()

    # --- draws --- (without updates)

    screen.fill(Colors.black)

    for item in circles:
        item.draw(screen)

    pygame.display.update()

    clock.tick(FPS)


pygame.quit() # close window    
