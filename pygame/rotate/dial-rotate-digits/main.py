#!/usr/bin/env python3

# date: 2020.01.25
# https://stackoverflow.com/questions/59902716/how-to-rotate-element-around-pivot-point-in-pygame  

import pygame
import time
import math

# --- constants --- (UPPER_CASE_NAMES)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800

# --- classes ---

class Dial:
    
    def __init__(self, x, y, radius, inputs, angle_step=45):
        self.rect = pygame.Rect(x-radius, y-radius, 2*radius, 2*radius)
        self.radius = radius
        self.radius2 = radius - 30 # position for digits
        self.inputs = inputs
        self.angle_step = angle_step

    def draw(self): # no need to add prefix/postfix 'Dial' to name `draw`
        #for i in range(0, self.columns):
        # `Dial` means single object so it should draw only one circle 
        pygame.draw.circle(window, RED, self.rect.center, self.radius)
        pygame.draw.circle(window, BLACK, self.rect.center, self.radius, 1)

        angle = 0
        for number in self.inputs:
            text = font.render(str(number), 1, BLACK)
            
            # rotate image
            text = pygame.transform.rotate(text, -angle)
            
            # center image on circle
            text_rect = text.get_rect(center=self.rect.center)
            
            # move using `angle` and `radius`
            angle_rad = math.radians(180-angle)
            text_rect.centerx += self.radius2 * math.sin(angle_rad)
            text_rect.centery += self.radius2 * math.cos(angle_rad)
            
            window.blit(text, text_rect)

            angle += self.angle_step

            
# --- functions ---

def level_1():
   window.fill(WHITE)
   dial1.draw()
   dial2.draw()
   dial3.draw()

# --- main ---

pygame.init()

window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
window_rect = window.get_rect()

pygame.display.set_caption("Dials")

clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 50, True)

#tutorial = [pygame.image.load('Dial_Images/tutorial_base.png')]

tutorial_inputs = [[1,4,3,4], [1,4,3,2], [1,4,3,2], [1,4,3,4]]

dial1 = Dial(window_rect.centerx, window_rect.centery, window_rect.centerx-250, tutorial_inputs[0], 45)
dial2 = Dial(window_rect.centerx-250, window_rect.centery-250, window_rect.centerx-250, tutorial_inputs[1], 90)
dial3 = Dial(window_rect.centerx+250, window_rect.centery-250, window_rect.centerx-250, tutorial_inputs[2], 30)

score = 0

run = True
level1 = True

while run:
    #keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(100)

    if level1:
        level_1()

pygame.quit()   
