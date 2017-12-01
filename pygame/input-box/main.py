import pygame

class InputBox():
    
    def __init__(self, x, y):
        
        self.font = pygame.font.SysFont(None, 32)

        self.rect = pygame.Rect(x, y, 140, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('black')
        self.color = self.color_inactive
        self.text = ''

        self.active = False
        
    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
    
    def draw(self, screen):
        text_image = self.font.render(self.text, True, self.color)
        text_rect = text_image.get_rect()
        self.rect.w = max(200, text_rect.w+10)

        screen.blit(text_image, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

def main():

    pygame.init()        
    screen = pygame.display.set_mode((800,600))

    widgets = [
        InputBox(50, 50),
        InputBox(450, 50),
        InputBox(50, 150),
        InputBox(450, 150),
        InputBox(50, 250),
        InputBox(450, 250),
        InputBox(50, 350),
        InputBox(450, 350),
    ]

    clock = pygame.time.Clock()
    running = True
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            for child in widgets:
                child.handle_event(event)
            
        screen.fill((128, 128, 128))

        for child in widgets:
            child.draw(screen)

        pygame.display.flip()
        
        clock.tick(15)
        
    pygame.quit()

main()
