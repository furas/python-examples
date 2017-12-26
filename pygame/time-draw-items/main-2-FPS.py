import pygame
import random

# --- constants ---

WHITE = (255, 255, 255)
SIDE = 600

# --- main ---

# - init -

pygame.init()

win = pygame.display.set_mode((SIDE, SIDE))

win.fill(WHITE)
pygame.display.update()

# - objects -

circles_number = 100

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            running = False
            
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
    
    # 2 frames per seconds = 2 circles per second
    clock.tick(2)
    
pygame.quit()
