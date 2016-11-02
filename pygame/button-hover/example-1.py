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

# === CONSTANTS === (UPPER_CASE names)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400

# === CLASSES === (CamelCase names)

class Button():

    def __init__(self, text, x=0, y=0, width=100, height=50, command=None):

        self.text = text
        self.command = command
        
        self.image_normal = pygame.Surface((width, height))
        self.image_normal.fill(GREEN)

        self.image_hovered = pygame.Surface((width, height))
        self.image_hovered.fill(RED)

        self.image = self.image_normal
        self.rect = self.image.get_rect()

        font = pygame.font.Font('freesansbold.ttf', 15)
        
        text_image = font.render(text, True, WHITE)
        text_rect = text_image.get_rect(center = self.rect.center)
        
        self.image_normal.blit(text_image, text_rect)
        self.image_hovered.blit(text_image, text_rect)

        # you can't use it before `blit` 
        self.rect.topleft = (x, y)

        self.hovered = False
        #self.clicked = False

    def update(self):

        if self.hovered:
            self.image = self.image_hovered
        else:
            self.image = self.image_normal
        
    def draw(self, surface):

        surface.blit(self.image, self.rect)

    def handle_event(self, event):

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                print('Clicked:', self.text)
                if self.command:
                    self.command()
                

# === FUNCTIONS === (lower_case names)

    # empty

# === MAIN === (lower_case names)

def main():

    # --- init ---

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_rect = screen.get_rect()

    clock = pygame.time.Clock()
    is_running = False

    btn1 = Button('Hello', 200, 50, 100, 50)
    btn2 = Button('World', 200, 150, 100, 50)

    # --- mainloop --- (don't change it)

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

            btn1.handle_event(event)
            btn2.handle_event(event)

        # --- updates ---

        btn1.update()
        btn2.update()

        # --- draws ---

        screen.fill(BLACK)

        btn1.draw(screen)
        btn2.draw(screen)

        pygame.display.update()

        # --- FPS ---

        clock.tick(25)

    # --- the end ---

    pygame.quit()


#----------------------------------------------------------------------

if __name__ == '__main__':

    main()
