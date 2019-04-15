
# date: 2019.04.09
# https://stackoverflow.com/questions/55592626/how-would-i-make-this-button-so-that-it-only-registers-one-click

import pygame

# --- constants ---

WIDTH = 640
HEIGHT = 480

FPS = 5

# --- functions ---

def action_button_click(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()

def action_button_draw(x, y, w, h, ic, ac, text, text_colour):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    font = pygame.font.SysFont("arial black",20)
    text = font.render(text,True,(text_colour))
    screen.blit(text,[x+w/2-(text.get_rect().w/2),y+h/2-(text.get_rect().h/2)])

def test_action():
    print("clicked")

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()

# - mainloop -

clock = pygame.time.Clock()
running = True

while running:

    # - events -

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        # MOUSEBUTTONDOWN is created only once,
        # when button changes state from "not-pressed" to "pressed"
        # so it is better for this job than "pygame.mouse.get_pressed()"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                action_button_click(100, 100, 100, 50, test_action)

    # --- draws ----

    screen.fill([0,0,0]) # clear screen

    action_button_draw(100, 100, 100, 50, [255,0,0], [0,255,0], "Hello", [0,0,0])

    pygame.display.flip()

    # - FPS -

    clock.tick(FPS)

# - end -

pygame.quit()
