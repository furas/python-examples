#!/usr/bin/env python

# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html#saving-a-video
# FFMPEG FOURCC tags: http://ffmpeg.org/doxygen/trunk/isom_8c-source.html
# FOURCC codecs: http://www.fourcc.org/codecs.php
# $ ffmpeg --codecs
# http://www.ftyps.com/

from __future__ import print_function
import cv2
import time
import os

# ---------------------------------------------------------------------

# keys 
KEY_R = ord('r') # start recording
KEY_S = ord('s') # stop recording
KEY_Q = ord('q') # quit
KEY_ESC = 27     # quit 

# font
FONT = cv2.FONT_HERSHEY_PLAIN

# video file size
VIDEO_FILE_SIZE = 10 * 1024 * 1024 # split to 10 MB files

# ---------------------------------------------------------------------

# states
running = True 
recording = False
create_new_file = True

# window name
window_name = time.strftime("%Y.%m.%d  %H.%M.%S", time.localtime())

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
    fps = 30.0 # use different value to get slowmotion or fastmotion effect
    
    print('VCAP width :', width)
    print('VCAP height:', height)
    print('VCAP fps   :', fps)
 
while running:
    # grab, decode and return the next video frame (and "return" status)
    ret, frame = vcap.read()
 
    # write the next video frame
    if recording:
        if create_new_file:
            # VideoWriter constructors
            #.mp4 = codec id 2
            filename = time.strftime("%Y.%m.%d  %H.%M.%S", time.localtime()) + ".avi"

            #fourcc = cv2.cv.CV_FOURCC(*'I420') # .avi
            #fourcc = cv2.cv.CV_FOURCC(*'MP4V') # .avi
            fourcc = cv2.cv.CV_FOURCC(*'MP42') # .avi
            #fourcc = cv2.cv.CV_FOURCC(*'AVC1') # error libx264
            #fourcc = cv2.cv.CV_FOURCC(*'H264') # error libx264
            #fourcc = cv2.cv.CV_FOURCC(*'WRAW') # error --- no information ---
            #fourcc = cv2.cv.CV_FOURCC(*'MPEG') # .avi 30fps
            #fourcc = cv2.cv.CV_FOURCC(*'MJPG') # .avi
            #fourcc = cv2.cv.CV_FOURCC(*'XVID') # .avi
            #fourcc = cv2.cv.CV_FOURCC(*'H265') # error 
            
            fout = cv2.VideoWriter(filename, fourcc, fps, (width, height))
            create_new_file = False
 
            # check if video writer has been successfully initialized
            if not fout.isOpened():
                print("ERROR INITIALIZING VIDEO WRITER")
                break
            else:
                print("OK INITIALIZING VIDEO WRITER")
 
        # write frame to file         
        if fout.isOpened():
            fout.write(frame)
 
        # check file size
        if os.path.getsize(filename) >= VIDEO_FILE_SIZE:
            fout.release() # close current file
            create_new_file = True # time to create new file in next loop
 
        # add REC to frame
        cv2.putText(frame, "REC", (40,40), FONT, 3 , (0,0,255), 2)
        cv2.circle(frame, (20,20), 10 , (0,0,255), -1)

    # displays an image in the specified window (without menu)
    #cv2.imshow(window_name, frame)         
 
    # add instruction to frame
    cv2.putText(frame,"R - START RECORDING",(width - 200,20), FONT, 1 ,(255,255,255))
    cv2.putText(frame,"S - STOP RECORDING",(width - 200,40), FONT, 1 ,(255,255,255))
    cv2.putText(frame,"Q - QUIT",(width - 200,60), FONT, 1 ,(255,255,255))
    cv2.putText(frame,"ESC - QUIT",(width - 200,80), FONT, 1 ,(255,255,255))
 
    # displays an image in the specified window (with menu)
    #cv2.namedWindow(window_name)
    cv2.imshow(window_name+' (with menu)', frame)         
 
    # get key (get only lower 8-bits to work with chars)
    key = cv2.waitKey(1) & 0xFF

    # check what to do
    if key == KEY_R and not recording:
        print("START RECORDING")
        recording = True
        create_new_file = True
    elif key == KEY_S and recording:
        print("STOP RECORDING")
        recording = False
        create_new_file = False
        fout.release()
    #elif key in (KEY_Q, KEY_ESC):
    elif key == KEY_Q or key == KEY_ESC:
        print("EXIT")
        running = False
 
#Release everything 
#fout.release()
vcap.release()
cv2.destroyAllWindows()
