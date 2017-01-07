#!/usr/bin/env python3

#
# Bartłomiej "furas" Burek
#
# doc: https://www.libsdl.org/release/SDL-1.2.15/docs/html/sdlenvvars.html
#

import os
import pygame

pygame.init()

# ---

print('pos: 50, 500')

os.environ['SDL_VIDEO_WINDOW_POS'] = '50, 500'

screen = pygame.display.set_mode((300,300), 32, pygame.NOFRAME)

pygame.time.delay(2000)

# ---

print('pos: 500, 50')

os.environ['SDL_VIDEO_WINDOW_POS'] = '500, 50'

screen = pygame.display.set_mode((300,300), 32, pygame.NOFRAME)

pygame.time.delay(2000)

# ---

print('pos: center')

del os.environ['SDL_VIDEO_WINDOW_POS']
os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = pygame.display.set_mode((300,300), 32, pygame.NOFRAME)

pygame.time.delay(2000)

# ---

pygame.quit()
