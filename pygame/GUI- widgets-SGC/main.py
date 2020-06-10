#!/usr/bin/env python3 

# date: 2019.11.25
# https://stackoverflow.com/questions/59018142/sgc-gui-and-pygame-widget-implementation

import glob
import pygame
import time

import sys

import sgc 
from sgc.locals import *

# --- constants --- (UPPER_CASE)

WHITE = (255, 255, 255) 

MAXNOTE = 10
MAXDURATION = 10

PATH = r'C:\Path'
PATH = '/home/furas/Obrazy/images'

# --- functions --- (lower_case_names)

def on_click_button():
    print('on_click_button')
    
# ---  main ---

filenames = sorted(glob.glob(PATH + "/*.png"))

print('len:', len(filenames))

names = []
images = []
for item in filenames:
    names.append("img" + item.replace(".png", "").replace("h", "."))
    images.append(pygame.image.load(item))

current_image = 0

# --- 

pygame.init()

display_surface = sgc.surface.Screen((400, 400))
#display_surface = pygame.display.set_mode((400, 400)) 
display_rect = display_surface.get_rect()    

font = pygame.font.Font('freesansbold.ttf', 32) 

btn = sgc.Button(label="Clicky", pos=(10, 10))#, label_font=font)
btn.add(0)
btn.on_click = on_click_button

# ---

clock = pygame.time.Clock()

current_time = pygame.time.get_ticks()
end_time = current_time + MAXDURATION*1000
end_slide = current_time

running = True
while running and ((current_time < end_time) or (current_image < MAXNOTE)):

    ticks = clock.tick(30)

    for event in pygame.event.get():
        sgc.event(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               running = False
    
    current_time = pygame.time.get_ticks()

    if (end_slide <= current_time) and (current_image < len(images)):
        image = images[current_image]
        image_rect = image.get_rect()     
        image_rect.center = display_rect.center

        end_slide = current_time + 2000 # 2000ms (2s)
        current_image += 1

        display_surface.fill(WHITE)
        display_surface.blit(image, image_rect)

    sgc.update(ticks)
    pygame.display.flip()

# ---

display_surface.fill(WHITE)

text = font.render('GeeksForGeeks', True, (0, 255, 0), (0, 0, 128))
text_rect = text.get_rect()
text_rect.center = display_rect.center
display_surface.blit(text, text_rect)

#pygame.display.update() # no need it
pygame.display.flip()

time.sleep(5)

# --- end ---

pygame.display.quit()

print("the end")
