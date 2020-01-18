#!/usr/bin/env python3

# date: 2020.01.17
# 

import pygame

# === CONSTANTS === (UPPER_CASE_NAMES)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

# === CLASSES === (CamelCaseNames)

class Player():

    def __init__(self, screen, config):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.config = config
        
        self.direction = 'right'
        self.rect = pygame.Rect(100, 100, 20, 20)
        self.speed = 10
    
    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

    def update(self):
        self.rect.x += self.speed
        if self.direction == 'right':
            if self.rect.right > self.screen_rect.right:
                self.rect.right = self.screen_rect.right
                self.speed = -self.speed
                self.direction = 'left'
        elif self.direction == 'left':
            if self.rect.left < self.screen_rect.left:
                self.rect.left = self.screen_rect.left
                self.speed = -self.speed
                self.direction = 'right'
    
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

    def exit(self):
        self.is_running = False
    
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


class IntroStage(Stage):

    def create_objects(self):
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("INTRO STAGE (Press ESC or Click Mouse)", True, BLACK)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.fill(GREEN)
        surface.blit(self.text, self.text_rect)
   
    def handle_event(self, event):
        # close on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #self.is_running = False
            self.exit()
            
class MenuStage(Stage):

    def create_objects(self):
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("MENU STAGE (Press ESC)", True, BLACK)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)
        self.text_rect.top = 10
        
        self.stage_game = GameStage(self.screen, self.config)
        self.stage_options = OptionsStage(self.screen, self.config)

        self.button1 = button_create("GAME", (300, 200, 200, 50), GREEN, BLUE, self.stage_game.mainloop)
        self.button2 = button_create("OPTIONS", (300, 300, 200, 50), GREEN, BLUE, self.stage_options.mainloop)
        self.button3 = button_create("EXIT", (300, 400, 200, 50), GREEN, BLUE, self.exit)
        
    def draw(self, surface):
        surface.fill(RED)
        surface.blit(self.text, self.text_rect)

        button_draw(surface, self.button1)
        button_draw(surface, self.button2)
        button_draw(surface, self.button3)

    def handle_event(self, event):
        button_check(self.button1, event)
        button_check(self.button2, event)
        button_check(self.button3, event)
            
class OptionsStage(Stage):

    def create_objects(self):
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("OPTIONS STAGE (Press ESC)", True, BLACK)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.fill(RED)
        surface.blit(self.text, self.text_rect)
      
        
class ExitStage(Stage):

    def create_objects(self):
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("EXIT STAGE (Press ESC or Click Mouse)", True, BLACK)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)

    def draw(self, surface):
        surface.fill(GREEN)
        surface.blit(self.text, self.text_rect)

    def handle_event(self, event):
        # close on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #self.is_running = False
            self.exit()
        
class GameStage(Stage):

    def create_objects(self):
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render("GAME STAGE (Press ESC)", True, BLACK)
        self.text_rect = self.text.get_rect(center=self.screen_rect.center)

        self.player = Player(self.screen, self.config)
                
    def draw(self, surface):
        surface.fill(BLUE)
        surface.blit(self.text, self.text_rect)
        self.player.draw(surface)
        
    def update(self):
        self.player.update()

# === FUNCTIONS === (lower_case_names)
# TODO: create class Button()

def button_create(text, rect, inactive_color, active_color, action):

    font = pygame.font.Font(None, 40)

    button_rect = pygame.Rect(rect)

    text = font.render(text, True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)

    return [text, text_rect, button_rect, inactive_color, active_color, action, False]


def button_check(info, event):

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if event.type == pygame.MOUSEMOTION:
        # hover = True/False
        info[-1] = rect.collidepoint(event.pos)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and action:
            action()

def button_draw(screen, info):

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if hover:
        color = active_color
    else:
        color = inactive_color

    pygame.draw.rect(screen, color, rect)
    screen.blit(text, text_rect)
        
# === MAIN === (lower_case_names)

class App():
    
    # --- init ---

    def __init__(self):

        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        config = {}
        
        stage = IntroStage(screen, config)
        stage.mainloop()
        
        stage = MenuStage(screen, config)
        stage.mainloop()
        
        stage = ExitStage(screen, config)
        stage.mainloop()

        pygame.quit()
        
    #def run(self):
        
#----------------------------------------------------------------------

if __name__ == '__main__':

    App() #.run()

