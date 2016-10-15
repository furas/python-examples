#!/usr/bin/env python3

#
# pygame (classes) template - by furas
#

# ---------------------------------------------------------------------

__author__  = 'Bartlomiej "furas" Burek'
__email__   = 'furas@tlen.pl'
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

BLOCK_SIZE = 50

# === CLASSES === (CamelCase names)

class Button():

    def __init__(self, pos):

        self.image_normal = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image_normal.fill(GREEN)

        self.image_hovered = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image_hovered.fill(RED)

        self.image = self.image_normal
        
        self.rect = self.image.get_rect(topleft=pos)
        #self.rect.center = screen_rect.center

        self.hovered = False
        self.clicked = False

    def update(self):

        if self.hovered:
            self.image = self.image_normal
        else:
            self.image = self.image_hovered
        
    def draw(self, surface):

        surface.blit(self.image, self.rect)

    def handle_event(self, event):

        if event.type == pygame.MOUSEMOTION:
            #if self.rect.collidepoint(event.pos)
            #    self.hovered = True
            #else:
            #    self.hovered = False
        
            self.hovered = self.rect.collidepoint(event.pos)

# === FUNCTIONS === (lower_case names)


    # empty

# === MAIN === (lower_case names)

class App():

    # --- (global) variables ---

        # empty

    # --- init ---

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()

        self.clock = pygame.time.Clock()
        self.is_running = False

        self.widgets = []

        self.create_objects()

    def quit(self):

        pygame.quit()

    # --- objects ---

    def create_objects(self):

        size = BLOCK_SIZE + 5
        
        for row in range(5):
            for col in range(5):
                btn = Button((size*col, size*row))
                self.widgets.append(btn)

    # --- functions ---

    def handle_event(self, event):
        for widget in self.widgets:
            widget.handle_event(event)

    def update(self):
        for widget in self.widgets:
            widget.update()

    def draw(self, surface):

        #surface.fill(BLACK)

        for widget in self.widgets:
            widget.draw(surface)

        #pygame.display.update()

    # --- mainloop --- (don't change it)

    def mainloop(self):

        self.is_running = True

        while self.is_running:

            # --- events ---

            for event in pygame.event.get():

                # --- global events ---

                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False

                # --- objects events ---

                self.handle_event(event)

            # --- updates ---

            self.update()

            # --- draws ---

            self.screen.fill(BLACK)

            self.draw(self.screen)

            pygame.display.update()

            # --- FPS ---

            self.clock.tick(25)

        # --- the end ---

        self.quit()

#----------------------------------------------------------------------

if __name__ == '__main__':

    App().mainloop()
