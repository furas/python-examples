#!/usr/bin/env python3

import pygame
import pygame.gfxdraw
from PIL import Image, ImageDraw

# --- constants ---

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
GREY  = (128, 128, 128)

PI = 3.1415

# --- main ----

pygame.init()
screen = pygame.display.set_mode((800,600))

# - generate PIL image -

pil_size = 300

pil_image = Image.new("RGBA", (pil_size, pil_size))
pil_draw = ImageDraw.Draw(pil_image)
#pil_draw.arc((0, 0, pil_size-1, pil_size-1), 0, 270, fill=RED)
pil_draw.pieslice((0, 0, pil_size-1, pil_size-1), 330, 0, fill=GREY)

# - convert to PyGame image -

mode = pil_image.mode
size = pil_image.size
data = pil_image.tobytes()

image = pygame.image.fromstring(data, size, mode)
image_rect = image.get_rect(center=screen.get_rect().center)

# - mainloop -

clock = pygame.time.Clock()
running = True

while running:

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(RED)
    #pygame.draw.arc(screen, BLACK, (300, 200, 200, 200), 0, PI/2, 1)
    #pygame.gfxdraw.pie(screen, 400, 300, 100, 0, 90, RED)
    #pygame.gfxdraw.arc(screen, 400, 300, 100, 90, 180, GREEN)
    screen.blit(image, image_rect)
    pygame.display.flip()

# - end -

pygame.quit()
