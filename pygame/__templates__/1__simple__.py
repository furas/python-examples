#!/usr/bin/env python3

#
# pygame (simple) template - by furas
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

'''
BLOCK_SIZE = 50
'''

# === CLASSES === (CamelCase names)

'''
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.center = screen_rect.center

        self.move_x = 0
        self.move_y = 0
        self.gravity = 1

        self.jump = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.jump -= self.gravity

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_x -= 10
            elif event.key == pygame.K_RIGHT:
                self.move_x += 10
            elif event.key == pygame.K_UP:
                self.move_y -= 10
            elif event.key == pygame.K_DOWN:
                self.move_y += 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
               self.move_x += 10
            elif event.key == pygame.K_RIGHT:
                self.move_x -= 10
            elif event.key == pygame.K_UP:
                self.move_y += 10
            elif event.key == pygame.K_DOWN:
                self.move_y -= 10
'''

# === FUNCTIONS === (lower_case names)

    # empty

# === MAIN === (lower_case names)

# --- (global) variables ---

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

'''
player = Player()
'''

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

        '''
        player.handle_event(event)
        '''

    # --- updates ---

    '''
    player.update()
    '''

    # --- draws ---

    screen.fill(BLACK)

    '''
    player.draw(screen)
    '''

    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()
