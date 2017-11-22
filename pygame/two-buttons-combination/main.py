#!/usr/bin/env python3

import pygame, sys

'''
Two buttons combination (combo).

First you have to click RED and later BLUE to close program
'''

# --- functions ---

def check_which_button_was_click(buttons, pos):
    
    for name, (rect, color) in buttons.items():
        if rect.collidepoint(pos):
            return name

# --- main ---

# - init -

screen = pygame.display.set_mode((350, 150))

# - objects -

buttons = {
    'RED':   (pygame.Rect(50, 50, 50, 50),  (255, 0, 0)),
    'GREEN': (pygame.Rect(150, 50, 50, 50), (0, 255, 0)),
    'BLUE':  (pygame.Rect(250, 50, 50, 50), (0, 0, 255)),
}

previous_button = None
current_button = None

# - mainloop -

clock = pygame.time.Clock()
running = True

while running:

    # - event -
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked_button = check_which_button_was_click(buttons, event.pos)
            if clicked_button is not None:
               previous_button = current_button
               current_button = clicked_button
            print(previous_button, current_button)


    # - updates -
    
    if previous_button == 'RED' and current_button == 'BLUE':
        print('correct buttons combination')
        previous_button = None
        current_button = None
        running = False

    # - draws -
    
    screen.fill((0,0,0))
    
    for rect, color in buttons.values():
        pygame.draw.rect(screen, color, rect)
        
    pygame.display.flip()
    
    # - FPS -
    
    clock.tick(5)
    
# - end -

pygame.quit()
