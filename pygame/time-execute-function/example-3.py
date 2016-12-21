#!/usr/bin/env python3

import pygame

# --- constants ---

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# --- classes ---

class Rectangle():

    def __init__(self, color, rect, time=1000, show=True):
        self.color = color
        self.rect = pygame.rect.Rect(rect)
        self.show = show
        self.time = time

        # list for tasks to execute with delay
        self.tasks = []

        # add task to do after 0 ms
        self.after(0, self.task_show)

    def draw(self, surface):
        if self.show:
            #surface.blit(self.image, self.rect)
            pygame.draw.rect(surface, self.color, self.rect)

    def after(self, delay, callback):
        '''add new task to list'''
        current_time = pygame.time.get_ticks()
        self.tasks.append((current_time+delay, callback))
        
    def update(self):
        self.update_tasks()
        
    def update_tasks(self):
        current_time = pygame.time.get_ticks()

        temp = []

        # execute tasks and keep only not executed
        for task_time, task_callback in self.tasks:
            if current_time >= task_time:
                task_callback(current_time)
            else:
                temp.append((task_time, task_callback))

        self.tasks = temp
        
    def task_show(self, current_time):
        self.show = True
        self.after(self.time, self.task_hide)

    def task_hide(self, current_time):
        self.show = False
        self.after(self.time, self.task_show)

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((800, 600))

# - objects -

# first time check at once
green_rect = Rectangle(GREEN, (0, 0, 100, 100), time=1000)
red_rect   = Rectangle(RED,   (100, 0, 100, 100), time=100)

# other

rect = pygame.Rect(0, 0, 50, 50)

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:
    
    # - events -
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
             running = False
             
    # - updates -
    
    # update object
    
    green_rect.update()
    red_rect.update()
    
    # other

    rect.center = pygame.mouse.get_pos()
    
    # - draws -

    screen.fill(BLACK)

    green_rect.draw(screen)
    red_rect.draw(screen)
    
    pygame.draw.rect(screen, WHITE, rect)

    pygame.display.flip()

    # - FPS -
    
    clock.tick(30)

# - end -

pygame.quit()
