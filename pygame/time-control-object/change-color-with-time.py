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

# get current time
current_time = pygame.time.get_ticks()

# first change after 250 ms
change_color_time = current_time + 250

# --- mainloop ---

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get current time 
    current_time = pygame.time.get_ticks()
    
    # check if it is time to change color
    if current_time >= change_color_time:
        # set new time to change color again
        change_color_time = current_time + 250
        # change color
        if color == RED:
            color = BLACK
        else:
            color = RED                    

    screen.fill(WHITE)
    pygame.draw.rect(screen, color, [300, 200, 100, 100], 0)
    pygame.display.flip()

    clock.tick(20)

pygame.quit()
