
# date: 2019.04.05
# https://stackoverflow.com/a/55533542/1832058

import pygame

black = (0,0,0)
white = (255,255,255)
gray  = (128,128,128)
red   = (255,0,0)

pygame.init()
gameDisplay = pygame.display.set_mode( (800,600))
clock = pygame.time.Clock()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf = smallText.render(msg, True, red)
    textRect = textSurf.get_rect()
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def change_draw_to_intro():
    global draw
    draw = draw_intro

def change_draw_to_other():
    global draw
    draw = draw_other

def change_draw_to_BE01():
    global draw
    draw = draw_BE01

def draw_BE01():
    gameDisplay.fill(white)
    #gameDisplay.blit(BE01Img,(0,0))
    button("BACK",350,450,100,50,black,gray,change_draw_to_intro)

def draw_intro():
    gameDisplay.fill(white)
    #gameDisplay.blit(introImg,(0,0))
    button("START",350,450,100,50,black,gray,change_draw_to_other)

def draw_other():
    gameDisplay.fill(white)
    #gameDisplay.blit(scene01Img,(0,0))
    button("1",200,450,100,50,black,gray,change_draw_to_BE01)
    
def quitgame():
    pygame.quit()
    quit()   

def game_loop():
    global draw
    
    draw = draw_intro
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
