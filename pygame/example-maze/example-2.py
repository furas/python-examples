#!/usr/bin/env python3

import pygame

# --- constants ---

W = 25
H = 25
M = 2

SIZE = (550, 500)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

FPS = 25

# --- classes ---

class Player:

    def __init__(self, row=0, col=0):
        # to keep position and size
        self.rect = pygame.Rect(0, 0, 20, 20)

        # set start position
        self.rect.center = 149, 14

        self.r = 10

        self.speed_x = 0
        self.speed_y = 0

        self.row = 0
        self.col = 0

        current_time = pygame.time.get_ticks()
        self.next_move = current_time
        self.move_delay = 200

    def convert():
        self.rect.center =  + self.col*W, M + self.row*H
        return

    def draw(self, screen):
        self.rect.topleft =  2+(W + M) * self.col + M, 2+((H + M) * self.row + M)
        pygame.draw.circle(screen, RED, self.rect.center, self.r)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.speed_x -= 1
            elif event.key == pygame.K_RIGHT:
                self.speed_x += 1
            elif event.key == pygame.K_UP:
                self.speed_y -= 1
            elif event.key == pygame.K_DOWN:
                self.speed_y += 1
            elif event.key == pygame.K_LSHIFT:
                self.move_delay = 10

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.speed_x += 1
            elif event.key == pygame.K_RIGHT:
                self.speed_x -= 1
            elif event.key == pygame.K_UP:
                self.speed_y += 1
            elif event.key == pygame.K_DOWN:
                self.speed_y -= 1
            elif event.key == pygame.K_LSHIFT:
                self.move_delay = 200

    def update(self):
        current_time = pygame.time.get_ticks()

        if current_time >= self.next_move:

            self.next_move = current_time + self.move_delay

            #print(self.speed_x, self.speed_y)

            # check first only 'x' and later only 'y'


            if self.speed_x:
                # create copy of position
                new_pos = self.rect.move(self.speed_x*27, 0)

                # check if "copy" is still in rectangles
                for rectangle in all_rectangles:
                    if new_pos.colliderect(rectangle):
                        # now you can set new position
                        self.rect.move_ip(self.speed_x*27, 0)
                        self.col += self.speed_x
                        # don't check other rectangles
                        rectangle.dot = False
                        break

            if self.speed_y:
                # create copy of position
                new_pos = self.rect.move(0, self.speed_y*27)

                # check if "copy" is still in rectangles
                for rectangle in all_rectangles:
                    if new_pos.colliderect(rectangle):
                        # now you can set new position
                        self.rect.move_ip(0, self.speed_y*27)
                        self.row += self.speed_y
                        # don't check other rectangles
                        rectangle.dot = False
                        break

class Floor:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = BLACK
        self.dot = True

        self.rect = pygame.Rect((W + M) * col + M, ((H + M) * row + M), W, H)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 1)
        if self.dot:
            pygame.draw.circle(screen, GREEN, self.rect.center, 5)

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode(SIZE)
screen_rect = screen.get_rect()

# - objects -

player = Player()

# create list with rectangles (but not draw them)

map = [
   "########  #######",
   "#      ####     #",
   "#      #  #     #",
   "#    ########   #",
   "######      #   #",
   "   #        #####",
   "   #          #  ",
   "   ############  ",
   "   ############  ",
   "   ############  ",
   "   ############  ",
]

all_rectangles = []

for r, row in enumerate(map):
    for c, item in enumerate(row):
        if item == '#':
            all_rectangles.append(Floor(r, c))

# - mainloop -

clock = pygame.time.Clock()
running = True

while running:

    # - events (without draws) -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        player.handle_event(event)

    # - updates (without draws) -

    player.update()
    # - draws (everything in one place) -

    screen.fill(WHITE)

    for rectangle in all_rectangles:
        rectangle.draw(screen)

    player.draw(screen)

    pygame.display.flip()

    # - FPS - keep the same speed on all computers -

    clock.tick(FPS)

# - end -

pygame.quit()
