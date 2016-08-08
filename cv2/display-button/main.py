#!/usr/bin/env python

from __future__ import print_function
import cv2


class Button(object):

    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.hover = False

    def handle_event(self, event):
        print(event)
        
    def draw(self, frame):
        if not self.hover:
            cv2.putText(frame, "REC", (40,40), FONT, 3 , (0,0,255), 2)
            cv2.circle(frame, (20,20), 10 , (0,0,255), -1)
        else:
            cv2.putText(frame, "REC", (40,40), FONT, 3 , (0,255,0), 2)
            cv2.circle(frame, (20,20), 10 , (0,255,0), -1)
        
# ---------------------------------------------------------------------

# keys 
KEY_ESC = 27

# font
FONT = cv2.FONT_HERSHEY_PLAIN

# ---------------------------------------------------------------------

button = Button('QUIT', 0, 0, 100, 30)
# states
running = True 

cv2.setMouseCallback("x", button.handle_event)

# ---------------------------------------------------------------------

# create VideoCapture
vcap = cv2.VideoCapture(0) # 0=camera
 
# check if video capturing has been initialized already
if not vcap.isOpened(): 
    print("ERROR INITIALIZING VIDEO CAPTURE")
    exit()
else:
    print("OK INITIALIZING VIDEO CAPTURE")
 
    # get vcap property 
    width = int(vcap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    height = int(vcap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    #fps = float(vcap.get(cv2.cv.CV_CAP_PROP_FPS))
    fps = 15.0 # use different value to get slowmotion or fastmotion effect
    
    print('VCAP width :', width)
    print('VCAP height:', height)
    print('VCAP fps   :', fps)
 
while running:
    # grab, decode and return the next video frame (and "return" status)
    ret, frame = vcap.read()

    if not ret:
        running = False
    else:
        # add REC to frame
        cv2.putText(frame, "REC", (40,40), FONT, 3 , (0,0,255), 2)
        cv2.circle(frame, (20,20), 10 , (0,0,255), -1)

        # add instruction to frame
        cv2.putText(frame,"ESC - QUIT",(width - 200,20), FONT, 1 ,(255,255,255))

        button.draw(frame)
        
        # displays frame
        cv2.imshow('x', frame)         
     
        # get key (get only lower 8-bits to work with chars)
        key = cv2.waitKey(1) & 0xFF

        if key == KEY_ESC:
            print("EXIT")
            running = False
     
# release everything 
vcap.release()
cv2.destroyAllWindows()
