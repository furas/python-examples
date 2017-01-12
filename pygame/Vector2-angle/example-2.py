#!/usr/bin/env python3

'''
angle between line from A to B and horizontal line
'''

#!/usr/bin/env python3

#
# pygame (empty) template - by furas
#

# ---------------------------------------------------------------------

__author__  = 'Bartlomiej "furas" Burek'
__webpage__ = 'http://blog.furas.pl'

# ---------------------------------------------------------------------

import pygame

# === CONSTANS === (UPPER_CASE names)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

# === CLASSES === (CamelCase names)

    # empty

# === FUNCTIONS === (lower_case names)

def angle(ax, ay, bx, by):

    print("  Math:", math.degrees(math.atan2(by - ay, bx - ax)))

    #a = pygame.math.Vector2( (ax, ay) )
    #b = pygame.math.Vector2( (bx, by) )
    # or
    a = pygame.math.Vector2(ax, ay)
    b = pygame.math.Vector2(bx, by)

    zero = pygame.math.Vector2()

    print('PyGame:', zero.angle_to(b-a))

    #a = pygame.math.Vector2( pygame.mouse.get_pos() )
    #b = pygame.math.Vector2( player.rect.center )


# === MAIN === (lower_case names)

# --- (global) variables ---

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

ax, ay = screen_rect.center

# --- mainloop ---

clock = pygame.time.Clock()
is_running = True

while is_running:

    # --- events ---

    for event in pygame.event.get():

        # --- global events ---

        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

        # --- objects events ---

            # empty

    # --- updates ---

    bx, by = pygame.mouse.pos()

    # --- draws ---

    screen.fill(BLACK)

    pygame.draw.line(screen, )

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()

