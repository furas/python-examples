
# date: 2019.04.05
# it tooks ~5 minutes to create it
# https://stackoverflow.com/questions/55505573/how-do-i-make-pygame-draw-along-all-points-on-a-line-between-2-points/55526786#55526786

import pygame

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

WIDTH = 800
HEIGHT = 600
FPS = 60


def airbrush(brushSize = 3):
    global prev_x
    global prev_y
    
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        x, y = pygame.mouse.get_pos()
        if x >= 0 and x <= WIDTH and y >= 0 and y <= HEIGHT:
            pygame.draw.circle(display, BLACK, (x - 5, y - 5), 10)
        # if there is previous point then draw missing points 
        if prev_x is not None:
            diff_x = x - prev_x
            diff_y = y - prev_y
            steps = max(abs(diff_x), abs(diff_y))
            # skip if distance is zero
            if steps > 0:
                dx = diff_x / steps
                dy = diff_y / steps
                for _ in range(steps):
                    prev_x += dx
                    prev_y += dy
                    pygame.draw.circle(display, BLACK, (round(prev_x - 5), round(prev_y - 5)), 10)

        prev_x = x
        prev_y = y
    else:
        prev_x = None
        prev_y = None
        
pygame.init()

display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)


clock = pygame.time.Clock()

display.fill(WHITE)

prev_x = None
prev_y = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    airbrush()
    pygame.display.update()
    clock.tick(FPS)
    

