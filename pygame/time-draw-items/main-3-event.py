import pygame
import random

# --- constants --- (UPPER_CASE_NAMES)

WHITE = (255, 255, 255)
SIDE = 600

DRAW_CIRCLE_EVENT = pygame.USEREVENT

# --- main ---

# - init -

pygame.init()

win = pygame.display.set_mode((SIDE, SIDE))

win.fill(WHITE)
pygame.display.update()

# - objects -

circles_number = 10

# run event periodically
pygame.time.set_timer(DRAW_CIRCLE_EVENT, 500) # 500ms = 0.5s

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False
        if event.type == DRAW_CIRCLE_EVENT:

            if circles_number > 0:

                radius = random.randrange(2, 15)
                r = random.randrange(256)
                g = random.randrange(256)
                b = random.randrange(256)
                x = random.randrange(0 + radius, SIDE - radius)
                y = random.randrange(0 + radius, SIDE - radius)
            
                pygame.draw.circle(win, (r, g, b), (x, y), radius)
                pygame.display.update()

                # counting down circles
                circles_number -= 1
            else:
                # disable events
                pygame.time.set_timer(DRAW_CIRCLE_EVENT, 0)
    
    clock.tick(25)
    
pygame.quit()
