#!/usr/bin/env python3

#
# http://stackoverflow.com/a/41479461/1832058
#

import pygame
import math

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60

# --- functions --- (lower_case names)

def draw_lines(screen, number, delta_angle, start_angle, width=1):

    angle = start_angle

    for i in range(number):

        radians = math.radians(angle-90)

        x = round(line_start[0] + math.cos(radians) * line_len)
        y = round(line_start[1] + math.sin(radians) * line_len)

        pygame.draw.line(screen, line_color, line_start, (x, y), width)

        angle += delta_angle

# --- main --- (lower_case names)

# - init -

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# - objects-

line_start = screen_rect.center
line_len = 200
line_color = WHITE

start_angle = 0

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

    # - updates (without draws) -

    start_angle += 0.5

    # - draws (without updates) -

    screen.fill(BLACK)

    draw_lines(screen, 8, 5, start_angle)

    pygame.display.flip()

    # - constant speed - FPS -

    clock.tick(FPS)

# - end -

pygame.quit()
