#!/usr/bin/env python3

# date: 2019.11.06
# https://stackoverflow.com/questions/58630700/utilising-the-pygame-mixer-music-get-endevent

import pygame
import tkinter as tk

def check_event():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            print('music end event')
            label['text'] = ''
            
    root.after(100, check_event)

def play():
    label['text'] = 'playing'
    pygame.mixer.music.play()

# --- main ---

pygame.init()    

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)
pygame.mixer.music.load('sound.wav')

root = tk.Tk()

label = tk.Label(root)
label.pack()

button = tk.Button(root, text='Play', command=play)
button.pack()

check_event()
root.mainloop()

pygame.quit()

