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

'''
BLOCK_SIZE = 50
'''

# === CLASSES === (CamelCase names)

'''
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50,50))
        self.image.fill(GREEN)

        self.rect = img.get_rect()
        self.rect.center = screen_rect.center
        
        self.move_x = 0
        self.move_y = 0
        self.gravity = 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.jump -= self.gravity

    def handle_event(event):

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

class Stage():
    
    # --- (global) variables ---

        # empty

    # --- init ---

    def __init__(self, screen, config):

        self.screen = screen
        self.config = config

        self.screen_rect = screen.get_rect()
        
        self.clock = pygame.time.Clock()
        self.is_running = False

        self.widgets = []
        
        self.create_objects()

    def quit(self):
        
        pass
        
    # --- objects ---
    
    def create_objects(self):

        '''
        self.player = Player()
        '''

        '''
        btn = Button(...)
        self.widgets.append(btn)
        '''
        
    # --- functions ---
    
    def handle_event(self, event):

        '''
        self.player.handle_event(event)
        '''

        '''
        for widget in self.widgets:
            widget.handle_event(event)
        '''
        
    def update(self, ):

        '''
        self.player.update()
        '''

        '''
        for widget in self.widgets:
            widget.update()
        '''

    def draw(self, surface):
        
        #surface.fill(BLACK)
        
        '''
        self.player.draw(surface)
        '''

        '''
        for widget in self.widgets:
            widget.draw(surface)
        '''
        
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


class StartScreen(Stage):

    def __init__(self, screen, config):
        Stage.__init__(self, screen, config)
        
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("START SCREEN: Press ESC", True, BLACK)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.fill(RED)
        surface.blit(self.text, self.text_rect)
        
class EndScreen(Stage):

    def __init__(self, screen, config):
        Stage.__init__(self, screen, config)
        
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("END SCREEN: Press ESC", True, BLACK)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.fill(GREEN)
        surface.blit(self.text, self.text_rect)
        
class Game(Stage):

    def __init__(self, screen, config):
        Stage.__init__(self, screen, config)
        
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("GAME: Press ESC", True, BLACK)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.fill(BLUE)
        surface.blit(self.text, self.text_rect)
        
# === MAIN === (lower_case names)

class App():
    
    # --- init ---

    def __init__(self):

        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        config = {}
        
        StartScreen(screen, config).mainloop()
        Game(screen, config).mainloop()
        EndScreen(screen, config).mainloop()

        pygame.quit()
        
    #def run(self):
        
#----------------------------------------------------------------------

if __name__ == '__main__':

    App() #.run()
