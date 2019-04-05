#!/usr/bin/env python3

import pygame
from threading import Thread
import socket
import struct # to send `int` as  `4 bytes`
import time   # for test

# --- constants ---

#address = ("192.168.1.158", 12801)
ADDRESS = ("localhost", 12801)

SURFACE_SIZE = (680, 480)

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)

# --- classes ---

class Streaming(Thread):

    def __init__(self):
        Thread.__init__(self)

        pygame.init()

        #pygame.camera.init()
        #self.cam = pygame.camera.Camera("/dev/video0", (680, 480))
        #self.cam.start()

        # create surface to imitate camera image
        self.image = pygame.Surface(SURFACE_SIZE)
        self.image_rect = self.image.get_rect()

        # create font to display text on surface
        self.font = pygame.font.Font(None, 50)

    def get_image(self):
        #return cam.get_image()

        # get current time as string
        current_time = time.strftime('%H:%M:%S.%s')

        # render surface with text (and center it)
        text = self.font.render(current_time, True, BLACK, GREEN)
        text_rect = text.get_rect(center=self.image_rect.center)

        # clear image and put new text
        self.image.fill(WHITE)
        self.image.blit(text, text_rect)

        return self.image
        
    def run(self):

        s = socket.socket()

        # solution for: "socket.error: [Errno 98] Address already in use"
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        s.bind(ADDRESS)
        s.listen(1)
        
        print("Wait for connection")

        try:
            sc, info = s.accept()
            print("Video client connected:", info)

            while True:
                # get image surface
                
                image = self.get_image()
                
                # convert surface to string
                
                img_str = pygame.image.tostring(image, 'RGB')

                print('len:', len(img_str))

                # send string size
                
                len_str = struct.pack('!i', len(img_str))
                sc.send(len_str)

                # send string image
                
                sc.send(img_str)

                # wait
                
                time.sleep(0.5)
                
        except Exception as e:
            print(e)
        finally:
            # exit
            print("Closing socket and exit")
            sc.close()
            s.close()
            pygame.quit()

# --- main ---

Streaming().run()


