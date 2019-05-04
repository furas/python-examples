import pygame

# --- constants ---

BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

# --- main ---

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen_rect = screen.get_rect()

rect = pygame.Rect(0, 0, 200, 200)
rect.center = screen_rect.center

active = False

# --- mainloop ---

clock = pygame.time.Clock()

running = True

while running:

    # --- events ---

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LSHIFT:
                active = not active

    # --- updates ---

    if active:
        color = GREEN
    else:
        color = RED

    # --- draws ---

    screen.fill((0,0,0))

    pygame.draw.rect(screen, color, rect)
    pygame.display.flip()

    clock.tick(5)

# --- end ---

pygame.quit()
