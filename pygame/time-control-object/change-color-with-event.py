import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

# --- start ---

pygame.init()
screen = pygame.display.set_mode((700, 500))

# start color
color = RED

# define own event type
CHANGE_COLOR = pygame.USEREVENT + 1
# create event every 250ms
pygame.time.set_timer(CHANGE_COLOR, 250) # 250ms

# --- mainloop ---

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if get event
        if event.type == CHANGE_COLOR:
            # change color
            if color == RED:
                color = BLACK
            else:
                color = RED
                
    screen.fill(WHITE)
    pygame.draw.rect(screen, color, [300, 200, 100, 100], 0)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
