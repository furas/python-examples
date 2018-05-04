import pygame
import pygame.camera

pygame.camera.init() # it replaces `Camera` with correct class
camera = pygame.camera.Camera('/dev/video0') # Linux camera

pygame.init()
screen = pygame.display.set_mode(camera.get_size())

camera.start()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    image = camera.get_image()
    screen.blit(image, (0, 0))
    pygame.display.flip()
    clock.tick(25)
            
camera.stop()

pygame.camera.quit()
pygame.quit()


