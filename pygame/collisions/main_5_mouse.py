#!/usr/bin/env python
#-*- coding: utf-8 -*-

# First version for stackoverflow.com
# http://stackoverflow.com/questions/20180594/pygame-collision-by-sides-of-sprite
# https://pl.python.org/forum/index.php?topic=5727.msg24549#msg24549

import pygame
 
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
 
GREY  = (128,128,128)
 
class Player():
 
    def __init__(self, name="A", x=0, y=0, width=150, height=150, keyboard=None, mouse_button=False):

        self.name = name
        
        # Rect uzywany przy sprawdzaniu kolizji - `rect` i `rect_ratio`
        self.rect = pygame.Rect(x, y, width, height)
 
        # dodatkowy Rect tylko do rysowania niebieskiego kwadratu
        self.rect_75 = pygame.Rect(x, y, width*0.75, height*0.75)
        self.rect_75.center=self.rect.center
 
        # dodatkowy Rect tylko do rysowania zielonego kwadratu
        self.rect_50 = pygame.Rect(x, y, width*0.5, height*0.5)
        self.rect_50.center=self.rect.center
 
        # grubosc kreski
        self.rect_75_size = 1
        self.rect_50_size = 1
        self.circle_size = 1
 
        # grubosc kreski
        self.rect_75_color = GREY
        self.rect_50_color = GREY
        self.circle_color  = GREY
 
        self.speed_x = 5
        self.speed_y = 5
 
        self.move_x = 0
        self.move_y = 0
 
        self.collision = [False] * 9
 
        self.font = pygame.font.SysFont("", 32)
        self.text = "";

        self.keyboard = keyboard
        self.mouse_button = mouse_button
        self.mouse_move = False

        
    def set_center(self, screen):
        self.rect.center = screen.get_rect().center

 
    def event_handler(self, event):
        if self.keyboard:
            if event.type == pygame.KEYDOWN:
                if event.key == self.keyboard['left']:
                    self.move_x -= self.speed_x
                elif event.key == self.keyboard['right']:
                    self.move_x += self.speed_x
                elif event.key == self.keyboard['up']:
                    self.move_y -= self.speed_y
                elif event.key == self.keyboard['down']:
                    self.move_y += self.speed_y
     
            elif event.type == pygame.KEYUP:
                if event.key == self.keyboard['left']:
                    self.move_x += self.speed_x
                elif event.key == self.keyboard['right']:
                    self.move_x -= self.speed_x
                elif event.key == self.keyboard['up']:
                    self.move_y += self.speed_y
                elif event.key == self.keyboard['down']:
                    self.move_y -= self.speed_y

        if self.mouse_button:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == self.mouse_button:
                    self.mouse_move = True
                    self.rect.center = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == self.mouse_button:
                    self.mouse_move = False
            elif event.type == pygame.MOUSEMOTION:
                if self.mouse_move:
                    self.rect.center = event.pos
                
        #print event

                
    def update(self):
        # przesuwanie wszystkich kwadratow
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.rect_75.center = self.rect.center
        self.rect_50.center = self.rect.center

 
    def draw(self, screen):
 
        # rysowanie dodatkowych kwadratow i okregu
        pygame.draw.rect(screen, self.rect_75_color, self.rect_75, self.rect_75_size)
        pygame.draw.rect(screen, self.rect_50_color, self.rect_50, self.rect_50_size)
        pygame.draw.circle(screen, self.circle_color, self.rect.center, self.rect.width/2, self.circle_size)
 
        # rysowanie bialego kwadratu i punktow
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        self.draw_point(screen, self.rect.topleft, self.collision[0])
        self.draw_point(screen, self.rect.topright, self.collision[1])
        self.draw_point(screen, self.rect.bottomleft, self.collision[2])
        self.draw_point(screen, self.rect.bottomright, self.collision[3])
 
        self.draw_point(screen, self.rect.midleft, self.collision[4])
        self.draw_point(screen, self.rect.midright, self.collision[5])
        self.draw_point(screen, self.rect.midtop, self.collision[6])
        self.draw_point(screen, self.rect.midbottom, self.collision[7])
 
        self.draw_point(screen, self.rect.center, self.collision[8])
 
 
    def draw_point(self, screen, pos, collision):
        if not collision:
            pygame.draw.circle(screen, GREEN, pos, 5)
        else:
            pygame.draw.circle(screen, RED, pos, 5)

 
    def check_collision(self, sprite):
        # sprawdzanie kolizji punktow w pelnym kwadracie
        self.collision[0] = sprite.rect.collidepoint(self.rect.topleft)
        self.collision[1] = sprite.rect.collidepoint(self.rect.topright)
        self.collision[2] = sprite.rect.collidepoint(self.rect.bottomleft)
        self.collision[3] = sprite.rect.collidepoint(self.rect.bottomright)
 
        self.collision[4] = sprite.rect.collidepoint(self.rect.midleft)
        self.collision[5] = sprite.rect.collidepoint(self.rect.midright)
        self.collision[6] = sprite.rect.collidepoint(self.rect.midtop)
        self.collision[7] = sprite.rect.collidepoint(self.rect.midbottom)
 
        self.collision[8] = sprite.rect.collidepoint(self.rect.center)
 
        # sprawdzanie kolizji niebieskich kwadratow
        if pygame.sprite.collide_rect_ratio(0.75)(self, sprite):
            self.rect_75_size = 3
            self.rect_75_color = BLUE
        else:
            self.rect_75_size = 1
            self.rect_75_color = GREY
 
        # sprawdzanie kolizji zielonych kwadratow
        if pygame.sprite.collide_rect_ratio(0.5)(self, sprite):
            self.rect_50_size = 3
            self.rect_50_color = GREEN
        else:
            self.rect_50_size = 1
            self.rect_50_color = GREY
 
        # sprawdzanie kolizji czerwonych okregow
        if pygame.sprite.collide_circle(self, sprite):
            self.circle_size = 3
            self.circle_color = RED
        else:
            self.circle_size = 1
            self.circle_color = GREY
 
 
    def render_collision_info(self):
 
        text = self.name + ": sides and corners: "
        #print "collision:",
 
        if self.collision[0] or self.collision[2] or self.collision[4]:
            text += "left "
            #print "left",
 
        if self.collision[1] or self.collision[3] or self.collision[5]:
            text += "right "
            #print "right",
 
        if self.collision[0] or self.collision[1] or self.collision[6]:
            text += "top "
            #print "top",
 
        if self.collision[2] or self.collision[3] or self.collision[7]:
            text += "bottom "
            #print "bottom",
 
        if self.collision[8]:
            text += "center "
            #print "center",
 
        #print
 
        self.text = self.font.render(text, 1, WHITE)
 
    def draw_collision_info(self, screen, pos):
        screen.blit(self.text, pos)
 
#----------------------------------------------------------------------
 
class Game():
 
    def __init__(self):
 
        pygame.init()
 
        self.screen = pygame.display.set_mode( (800,600) )
        pygame.display.set_caption("PyGame Collisions")
        
        self.player = Player(
            name = "A",
            keyboard={
                'left': pygame.K_LEFT,
                'right': pygame.K_RIGHT,
                'up': pygame.K_UP,
                'down': pygame.K_DOWN,
            },
            mouse_button=1, # left button
        )
        
        self.enemy  = Player(
            name = "B",
            keyboard={
                'left': pygame.K_a,
                'right': pygame.K_d,
                'up': pygame.K_w,
                'down': pygame.K_s,
            },
            mouse_button=3, # right button
        )
        
        self.enemy.set_center(self.screen)
 
        self.font = pygame.font.SysFont("", 32)
        self.text = ''
 
 
    def check_collisions(self):
        # sprawdzanie kolizji aby wypisywac informacje
 
        text = 'figures: '
 
        if pygame.sprite.collide_rect(self.player, self.enemy):
            text += 'white rect'
 
        if pygame.sprite.collide_rect_ratio(0.75)(self.player, self.enemy):
            text += ', blue rect (ratio:0.75)'
 
        if pygame.sprite.collide_rect_ratio(0.5)(self.player, self.enemy):
            text += ', green rect (ratio:0.50)'
 
        if pygame.sprite.collide_circle(self.player, self.enemy):
            text += ', red circle'
 
        self.text = self.font.render(text, 1, WHITE)
 
 
    def draw_collisions_info(self, screen, pos):
        screen.blit(self.text, pos)
 
 
    def run(self):
        clock = pygame.time.Clock()
 
        running = True
 
        while running:
 
            # --- events ----
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
 
                self.player.event_handler(event)
                self.enemy.event_handler(event)
 
            # --- updates ---
 
            self.player.update()
            self.enemy.update()
 
            self.player.check_collision(self.enemy)
            self.enemy.check_collision(self.player)
            self.player.render_collision_info()
            self.enemy.render_collision_info()
 
            self.check_collisions()
 
            # --- draws ----
 
            self.screen.fill(BLACK)
 
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
 
            self.player.draw_collision_info(self.screen, (0,0))
            self.enemy.draw_collision_info(self.screen, (0,32))
 
            self.draw_collisions_info(self.screen, (0, 600-32))
 
            pygame.display.update()
 
            # --- FPS ---
 
            clock.tick(30)
 
        pygame.quit()
 
#----------------------------------------------------------------------
 
Game().run()
