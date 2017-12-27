import pygame

# --- constants --- (UPPER_CASE_NAMES)

# - colors -

BACKGROUND_0 = (36, 38, 82)
BACKGROUND_1 = (40, 42, 86)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 47, 47)
GREEN = (79, 255, 101)

WOOD = (253, 197, 136)
PIPE = (152, 228, 86)
END = (137, 226, 57)
GOLD = (219, 178, 58)
GOLDEN = (254, 197, 34)
GOLDER = (255, 206, 63)

# - states -

STATE_INTRO    = 1
STATE_GAME     = 2
STATE_GAMEOVER = 3

# --- classes --- (CamelCaseNames)

#class Wall(pygame.sprite.Sprite):
#
#   def __init__(self, x, y, width, height):
#        super().__init__()
#
#        self.image = pygame.Surface((width, height))
#        self.image.fill(GREY)
#
#        self.rect = self.image.get_rect()
#        self.rect.y = y
#        self.rect.x = x

# --- functions --- (lower_case_names)

# empty

# --- main ---

# - init -

pygame.init()
screen = pygame.display.set_mode((1400,700))

font1 = pygame.font.SysFont("Berlin Sans FB Demi", 100, True, False)
text1 = font1.render("You Lost", True, BLACK)
font2 = pygame.font.SysFont("Aharoni", 50, True, False)
text2 = font2.render("RESET", True, WHITE)

# - objects -

player_y = 200
player_x = 10

x_change = 5
y_change = 0

all_pipes = [
    #upper pipes
    (END, pygame.Rect(195,300,80,40)), 
    (PIPE, pygame.Rect(200,0,70,300)), 
    (PIPE, pygame.Rect(350,0,70,450)), 
    (END, pygame.Rect(345,420,80,40)), 
    (PIPE, pygame.Rect(490,0,70,480)), 
    (END, pygame.Rect(485,480,80,40)), 
    (PIPE, pygame.Rect(630,0,70,450)), 
    (END, pygame.Rect(625,450,80,40)), 
    (PIPE, pygame.Rect(770,0,70,430)), 
    (END, pygame.Rect(765,420,80,40)), 
    (PIPE, pygame.Rect(910,0,70,400)), 
    (END, pygame.Rect(905,400,80,40)), 
    (PIPE, pygame.Rect(1050,0,70,470)), 
    (END, pygame.Rect(1045,470,80,40)), 
    (PIPE, pygame.Rect(1190,0,70,430)), 
    (END, pygame.Rect(1185,430,80,40)), 
    (GOLD, pygame.Rect(1330,0,70,410)), 
    (GOLDER, pygame.Rect(1350,0,70,410)), 
    (GOLDEN, pygame.Rect(1325,410,80,40)), 
    (PIPE, pygame.Rect(200,400,70,240)), 
    #lower pipes
    (END, pygame.Rect(195,400,80,40)), 
    (PIPE, pygame.Rect(350,520,70,500)), 
    (END, pygame.Rect(345,515,80,40)), 
    (PIPE, pygame.Rect(490,570,70,100)), 
    (END, pygame.Rect(485,570,80,40)), 
    (PIPE, pygame.Rect(630,570,70,100)), 
    (END, pygame.Rect(625,540,80,40)), 
    (PIPE, pygame.Rect(770,550,70,120)), 
    (END, pygame.Rect(765,510,80,40)), 
    (PIPE, pygame.Rect(910,530,70,220)), 
    (END, pygame.Rect(905,490,80,40)), 
    (PIPE, pygame.Rect(1050,560,70,220)), 
    (END, pygame.Rect(1045,560,80,40)), 
    (PIPE, pygame.Rect(1190,530,70,220)), 
    (END, pygame.Rect(1185,530,80,40)), 
    (GOLD, pygame.Rect(1330,530,70,220)), 
    (GOLDER, pygame.Rect(1350,530,70,220)), 
    (GOLDEN, pygame.Rect(1325,510,80,40)), 
    (WOOD, pygame.Rect(0,650,1400,50)), 
    (GREEN, pygame.Rect(0,640,1400,10)), 
]

# - mainloop -

state = STATE_INTRO # STATE_GAME, STATE_GAMEOVER

clock = pygame.time.Clock()
done = False

while not done:
    
    # - events -
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if state == STATE_INTRO:
            if event.type == pygame.KEYDOWN:
               state = STATE_GAME
               
        elif state == STATE_GAME:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_change = -5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    y_change = 5

        elif state == STATE_GAMEOVER:
            if event.type == pygame.KEYDOWN:
               state = STATE_INTRO
               player_y = 200
               player_x = 10

    # - updates (without draws) -
    
    if state == STATE_GAME:
        player_x += x_change
        player_y += y_change

        # check collisions with all pipes
        
        for pipe_color, pipe_rect in all_pipes:
            if pipe_rect.collidepoint(player_x, player_y):
                state = STATE_GAMEOVER
                break # no need to check other
    
    # - draws (without updates) -
    
    if state in (STATE_INTRO, STATE_GAME):
        screen.fill(BACKGROUND_0)
        pygame.draw.rect(screen, BACKGROUND_1, (0, 350, 1400, 350), 0)

        # draw all pipes

        for pipe_color, pipe_rect in all_pipes:
            pygame.draw.rect(screen, pipe_color, pipe_rect, 0)
            
        pygame.draw.circle(screen, WHITE, (player_x, player_y), 5)

    if state == STATE_GAMEOVER:
        screen.fill(WHITE)
        screen.blit(text1, (500, 100))
        pygame.draw.rect(screen, GREEN, (600, 400, 190, 60), 0)
        screen.blit(text2, (630, 410))

    pygame.display.update()
    clock.tick(25)
    
# - end -
    
pygame.quit()
