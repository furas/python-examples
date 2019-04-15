
# date: 2019.04.09
# https://stackoverflow.com/questions/55588557/how-to-move-a-circle-again-after-being-idle-for-3-seconds

import pygame

# --- constants ---

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# --- classes ---

# empty

# --- functions ---

# empty

# --- main ---

pygame.init()

windowCalibration = pygame.display.set_mode((0,0))
pygame.display.set_caption("Eye calibration")

circles = [
    {'pos': [300, 368], 'speed': 1, 'state': 'move_left', 'wait_to': 0, 'color': RED},
    {'pos': [300, 268], 'speed': 10, 'state': 'move_right', 'wait_to': 0, 'color': GREEN},
    {'pos': [300, 168], 'speed': 30, 'state': 'move_right', 'wait_to': 0, 'color': BLUE},
]

done = False
while not done:

    # --- events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    # --- moves ---
 
    current_time = pygame.time.get_ticks()

    for circle in circles:
        if circle['state'] == 'move_left':
            if circle['pos'][0] >= 10:
                circle['pos'][0] -= circle['speed']
            else:
                circle['pos'][0] = 10
                circle['state'] = 'wait_before_move_right'
                circle['wait_to'] = pygame.time.get_ticks() + 3000

        elif circle['state'] == 'move_right':
            if circle['pos'][0] <= 1350:
                circle['pos'][0] += circle['speed']
            else:
                circle['pos'][0] = 1350
                circle['state'] = 'wait_before_move_left'
                circle['wait_to'] = pygame.time.get_ticks() + 3000

        elif circle['state'] == 'wait_before_move_right':
            if current_time > circle['wait_to']:
                circle['state'] = 'move_right'

        elif circle['state'] == 'wait_before_move_left':
            if current_time > circle['wait_to']:
                circle['state'] = 'move_left'

    # --- draws ----

    windowCalibration.fill(WHITE)

    for circle in circles:
        pygame.draw.circle(windowCalibration, circle['color'], circle['pos'], 10)

    pygame.display.update()

# --- end ---

pygame.quit()
