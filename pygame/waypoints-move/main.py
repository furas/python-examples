#!/usr/bin/env python3

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

class Player():
    
    def __init__(self, waypoints, loop=False):
        
        # create green circe 
        r = 10
        
        self.image = pygame.Surface((2*r, 2*r)).convert_alpha()
        self.rect = self.image.get_rect()

        self.image.fill((0,0,0,0))
        pygame.draw.circle(self.image, (0,255,0), (r, r), r)

        # ---

        self.loop = loop
        
        self.speed = 5

        self.waypoints = waypoints
        self.next_point = 0

        # set current position
        # I use Vector2 because it keeps position as float numbers 
        # and it makes calcuations easier and more precise
        self.current = pygame.math.Vector2(self.waypoints[0])
        
        # set position in rect to draw it
        self.rect.center = self.current

        # set end point if exists on list
        self.target_index = 1
        if self.target_index < len(self.waypoints) - 1:
            self.target = pygame.math.Vector2(self.waypoints[self.target_index])
            self.moving = True
        else:
            self.target = self.current
            self.moving = False

    def move(self):
        
        if self.moving:

            # get distance to taget
            distance = self.current.distance_to(self.target)
            
            # 
            if distance > self.speed:
                self.current = self.current + (self.target - self.current).normalize() * self.speed
                self.rect.center = self.current
            else:
                # put player in tagert place, 
                # and find new target on list with waypoints 
                
                self.current = self.target
                self.rect.center = self.current
                
                # set next end point if exists on list
                self.target_index += 1
                if self.target_index < len(self.waypoints):
                    self.target = pygame.math.Vector2(self.waypoints[self.target_index])
                else:
                    if self.loop:
                        self.target_index = 0
                    else:
                        self.moving = False
                
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
# === MAIN === (lower_case names)

# --- init ---

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# --- objects ---

start = pygame.math.Vector2(screen_rect.centerx, screen_rect.bottom)
end = start
length = 150

waypoints = [(50, 50), (400, 150), (500, 50), (450, 350), (200, 200), (100, 350), (50, 50)]

player = Player(waypoints, True)

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

        # empty

    player.move()
    
    # --- draws ---

    screen.fill(BLACK)

    for start, end in zip(waypoints, waypoints[1:]):
        pygame.draw.line(screen, RED, start, end)

    player.draw(screen)
    
    pygame.display.update()

    # --- FPS ---

    clock.tick(25)

# --- the end ---

pygame.quit()
