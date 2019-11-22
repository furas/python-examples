#!/usr/bin/env python3

# date: 2019.11.06
# https://stackoverflow.com/questions/58630700/utilising-the-pygame-mixer-music-get-endevent

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

pygame.mixer.music.load('sound.wav')
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MUSIC_END:
            print('music end event')
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            # play again
            pygame.mixer.music.play()

pygame.quit()
