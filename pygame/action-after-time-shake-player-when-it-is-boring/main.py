
# https://www.pygame.org/docs/
#
# https://github.com/furas/python-examples/

import pygame
import random

# --- constants --- (UPPER_CASE_NAMES)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 25 # for more than 220 it has no time to update screen

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# --- classes --- (CamelCaseNames)

class Player(pygame.sprite.Sprite):

    def __init__(self, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2):
        super().__init__()
        
        self.image_white = pygame.Surface((100,100))
        self.image_white.fill(WHITE)

        self.image_red_face = pygame.Surface((100,100))
        self.image_red_face.fill(RED)
        # left eye
        pygame.draw.rect(self.image_red_face, BLACK, (20,20,10,10))
        # right eye
        pygame.draw.rect(self.image_red_face, BLACK, (70,20,10,10))
        # mouth
        pygame.draw.rect(self.image_red_face, BLACK, (30,60,40,10))
        # mouth left corner
        pygame.draw.rect(self.image_red_face, BLACK, (20,70,10,10))
        # mouth right corner
        pygame.draw.rect(self.image_red_face, BLACK, (70,70,10,10))

        self.image = self.image_white
        self.rect = self.image.get_rect(centerx=x, centery=y)

    def update(self):
        #move_x = random.randint(-5, 5)
        #move_y = random.randint(-5, 5)
        #self.rect.move_ip(move_x,move_y)
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def start_action(self):
        # save original position
        self.old_center = self.rect.center
        # change image
        self.image = self.image_red_face
        
    def action(self):
        # random move
        self.rect.y -= random.randint(-5, 5)

    def end_action(self):
        # restore original position
        self.rect.center = self.old_center
        # change image
        self.image = self.image_white
        
# --- functions --- (lower_case_names)

# --- main ---

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

player = Player()

# --- mainloop ---

clock = pygame.time.Clock()

# default values at start
do_something = False
time_since_last_action = 0

running = True
while running:
    # --- FPS ---

    dt = clock.tick(30)
    time_since_last_action += dt

    # --- events ---

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    moved = False

    if keys[pygame.K_LEFT]:
        player.rect.x -= 10 # player.rect.width
        moved = True
        # reset other values
        #do_something = False
        time_since_last_action = 0
    elif keys[pygame.K_RIGHT]:
        player.rect.x += 10 # player.rect.width
        moved = True
        # reset other values
        #do_something = False
        time_since_last_action = 0

    if not do_something and not moved and time_since_last_action > 1000:
        do_something = True
        player.start_action()
        # reset other values
        time_since_last_action = 0

    if do_something and not moved:
        #----action----
        player.action()

    if do_something and moved:
        do_something = False
        player.end_action()
        # reset other values
        time_since_last_action = 0
        
    # --- changes/moves/updates ---

    #if not pygame.key.get_pressed()[pygame.K_SPACE]:
    #    player.update()

    # --- draws ---

    screen.fill(BLACK)
    
    player.draw(screen)
    
    pygame.display.flip()
    
# --- end ---

pygame.quit()
 
            

