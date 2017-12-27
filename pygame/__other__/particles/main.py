import pygame
import sys
import random
import math

# --- constants ---- (UPPER_CASE_NAMES)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

FPS = 30

# --- classes --- (CamelCaseNames)

class Particle:

    def __init__(self, x, y, color=BLUE, radius=4, speed=0, angle=0):
        
        self.color = color
        self.radius = radius
        self.speed = speed
        self.angle = angle
        
        self.image = pygame.Surface((radius*2, radius*2)).convert()
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        
        self.rect = self.image.get_rect(centerx=x, centery=y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def update(self, surface_rect):

        self.dx = math.sin(self.angle) * self.speed
        self.dy = math.cos(self.angle) * self.speed

        self.rect.x += self.dx
        self.rect.y -= self.dy
 
        if self.rect.right >= surface_rect.right:
           self.rect.right = surface_rect.right
           self.angle = -self.angle
        elif self.rect.left <= surface_rect.left:
           self.rect.left = surface_rect.left
           self.angle = -self.angle
         
        if self.rect.bottom >= surface_rect.bottom:
           self.rect.bottom = surface_rect.bottom
           self.angle = math.pi - self.angle
           
        elif self.rect.top <= surface_rect.top:
           self.rect.top = surface_rect.top
           self.angle = math.pi - self.angle

# --- functions --- (lower_case_names)

def collide(p1, p2):
    
    dx = p1.rect.x - p2.rect.x
    dy = p1.rect.y - p2.rect.y
   
    distance = math.hypot(dx, dy)
   
    if distance < p1.radius + p2.radius:
        tangen = math.atan2(dy, dx)
        angle = math.pi/2 + tangen
        #print('angle:', math.degrees(angle))
         
        #print('before:', math.degrees(p1.angle),math.degrees(p2.angle))
        p1.angle = 2*tangen - p1.angle
        p2.angle = 2*tangen - p2.angle
        #print(' after:', math.degrees(p1.angle),math.degrees(p2.angle))
        #print('-----')

# --- main ---

number_of_particles = 100
particles = []

# - init -

pygame.init()
 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# - objects - 
 
for n in range(number_of_particles):
    #margin = random.randint(10, 50)
    margin = 10
    x  = random.randint(margin, SCREEN_WIDTH-margin)
    y  = random.randint(margin, SCREEN_HEIGHT-margin)
    speed = 4
    angle = random.uniform(0, 2*math.pi)
    color = random.choice([RED, GREEN, BLUE])
    
    item = Particle(x, y, speed=speed, angle=angle, color=color)
    particles.append(item)

item = Particle(100, 100, speed=2, angle=math.radians(-45+180), color=RED)
particles.append(item)

item = Particle(300, 300, speed=2, angle=math.radians(-45), color=GREEN)
particles.append(item)

# - mainloop -

speed = 0

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP:
                speed += 1
            elif event.key == pygame.K_DOWN:
                speed -= 1
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed = 0
            elif event.key == pygame.K_DOWN:
                speed = 0
 
    screen.fill(BLACK)
   
    #partikel.api = 1 #masih g bisa
    for i, item1 in enumerate(particles):
        item1.speed += speed
        item1.update(screen_rect)
        item1.draw(screen)
        for item2 in particles[i+1:]:
            collide(item1, item2)
   
    pygame.display.update()
    clock.tick(FPS)
