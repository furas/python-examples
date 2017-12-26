import pygame

# --- constants ---

WIDTH = 320
HEIGHT = 110

FPS = 5

# --- class ---

class Button(object):

    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0,0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center
        
        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

def stage1(screen):

    button1 = Button((5, 5), (100, 100), (0,255,0), "GO 1")
    button2 = Button((215, 5), (100, 100), (0,255,0), "EXIT")

    # - mainloop -
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
    
        # - events -
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    
            if button1.is_clicked(event):
                # go to stage2
                stage2(screen)
            if button2.is_clicked(event):
                # exit
                pygame.quit()
                exit()
   
        # - draws -

        screen.fill((255,0,0))    
        button1.draw(screen)
        button2.draw(screen)
        pygame.display.flip()
    
        # - FPS -
    
        clock.tick(FPS)

def stage2(screen):

    button1 = Button((5, 5), (100, 100), (255,0,0), "GO 2")
    button2 = Button((215, 5), (100, 100), (255,0,0), "BACK")

    # - mainloop -
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
    
        # - events -
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    
            if button1.is_clicked(event):
                stage3(screen)
            if button2.is_clicked(event):
                return
    
        # - draws -
    
        screen.fill((0,255,0))    
        button1.draw(screen)
        button2.draw(screen)
        pygame.display.flip()
    
        # - FPS -
    
        clock.tick(FPS)
    
def stage3(screen):

    button2 = Button((215, 5), (100, 100), (0,0,255), "BACK")

    # - mainloop -
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
    
        # - events -
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
    
            if button2.is_clicked(event):
                return
    
        # - draws -
    
        screen.fill((128,128,128))    
        button2.draw(screen)
        pygame.display.flip()
    
        # - FPS -
    
        clock.tick(FPS)
    
# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# - start -

stage1(screen)

# - end -

pygame.quit()
