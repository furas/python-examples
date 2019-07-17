
# date: 2019.07.10

import random
import pygame 
import pygame.mixer

library = ['Muzyka/snow2.mp3', "Muzyka/snow.wav"]
filename = random.choice(library)
print(filename)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.50)
pygame.mixer.music.load(filename)
pygame.mixer.music.play()
