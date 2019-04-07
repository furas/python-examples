
# date: 2019.04.06
#
# This version displays directly on screen so window must have the same size as stream


import pygame
import cv2

# --- local (built-in) camera ---
#stream = 0

# --- local file ---
#stream = '2019-03-26_08-43-15.mkv'

# --- http stream ---
# doesn't work any more
#stream = 'http://media.dumpert.nl/tablet/9f7c6290_Verstappen_vs._Rosberg_with_Horner_Smile___Streamable.mp4.mp4.mp4'

# --- rtsp stream ---
#stream = 'rtsp://streaming1.osu.edu/media2/ufsap/ufsap.mov'

# --- rtmp stream ---
# Big Buck Bunny
stream = 'rtmp://184.72.239.149/vod/mp4:bigbuckbunny_1500.mp4'

cap = cv2.VideoCapture(stream)

ret, img = cap.read()
if not ret:
    print("Can't read stream")
    #exit()

img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#img = cv2.transpose(img)
print('shape:', img.shape)

pygame.init()

screen = pygame.display.set_mode((img.shape[0], img.shape[1]))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    ret, img = cap.read()
    if not ret:
        running = False
        break
    else:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        #img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #img = cv2.transpose(img)
    
        pygame.surfarray.blit_array(screen, img)

    pygame.display.flip()

pygame.quit()
