#!/usr/bin/env python3


import pygame

# --- constants --- (UPPER_CASE names)

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

YELLOW = (255,255, 0)

# --- functions ---

def button_create(text, rect, inactive_color, active_color, action):

    font = pygame.font.Font(None, 40)

    button_rect = pygame.Rect(rect)

    text_buy = font.render(text, True, BLACK)
    text_buy_rect = text_buy.get_rect(center=button_rect.center)

    return [text_buy, text_buy_rect, button_rect, inactive_color, active_color, action, False]


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

# ---

def buy(number=1):
    global total
    
    total += number
    
    print('(+{}) total: {}'.format(number, total))

def buy_1():
    buy(1)
    
def buy_10():
    buy(10)

def buy_100():
    buy(100)

# --- main ---

# - init -

pygame.init()
screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()

# - objects -

total = 0

button_1 = button_create("+1", (380, 235, 75, 75), RED, GREEN, buy_1)
button_2 = button_create("+10", (480, 235, 75, 75), RED, GREEN, lambda:buy(10))
button_3 = button_create("+100", (580, 235, 75, 75), RED, GREEN, lambda:buy(100))

# - mainloop -

shop = True

while shop:
    
    # - events -
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shop = False

        button_check(button_1, event)
        button_check(button_2, event)
        button_check(button_3, event)
        
    # --- draws ---
    
    screen.fill(WHITE)

    button_draw(screen, button_1)
    button_draw(screen, button_2)
    button_draw(screen, button_3)

    pygame.display.update()
    
# - end -

pygame.quit()
