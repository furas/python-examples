import pygame

# --- constants ---

BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)

SCREEN_WIDTH  = 300
SCREEN_HEIGHT = 200

FPS = 5  # `FPS = 25` is enough for human eye to see animation.
         # If program don't use animation
         # then `FPS = 5` or even `FPS = 1` can be enough.

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# - objects -

font = pygame.font.SysFont(None, 30)

text = ""

text_image = font.render(text, True, GREEN)
text_rect = text_image.get_rect()     # get current size
text_rect.center = screen_rect.center # center on screen

# - mainloop -

clock = pygame.time.Clock()

done = False

while not done:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            text += event.unicode

            text_image = font.render(text, True, GREEN)
            text_rect = text_image.get_rect()     # get current size
            text_rect.center = screen_rect.center # center on screen

    # - draws -

    screen.fill(BLACK)

    screen.blit(text_image, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

# - end -
pygame.quit()
