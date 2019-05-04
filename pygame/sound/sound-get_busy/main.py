
# date: 2019.05.02
# author: Bartłomiej 'furas' Burek

import pygame
import time

pygame.init()

s = pygame.mixer.Sound('snow.wav')
s.play()

seconds = 0

while pygame.mixer.get_busy():
    time.sleep(1)
    seconds += 1
    print('seconds', seconds)
    if seconds >= 5:
        s.stop()

