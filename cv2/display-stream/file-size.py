#!/usr/bin/env python

import cv2

# --- local file ---
#stream = 'video.avi'

# --- http stream ---
#stream = 'http://media.dumpert.nl/tablet/9f7c6290_Verstappen_vs._Rosberg_with_Horner_Smile___Streamable.mp4.mp4.mp4'

# --- rtsp stream ---
#stream = 'rtsp://granton.ucs.ed.ac.uk/domsdemo/v2003-1.wmv'
#stream = 'rtsp://streaming1.osu.edu/media2/ufsap/ufsap.mov'

# --- local (build-in) camera ---
#stream = 0

# http://docs.opencv.org/2.4.13/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get

vcap = cv2.VideoCapture(stream)
 
if vcap.isOpened(): 
    # get vcap property
    width = vcap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)   # float
    height = vcap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT) # float
    print(width, height)
    
    # or
    width = vcap.get(3)  # float
    height = vcap.get(4) # float
    print(width, height)
   
    # camera: -1.0
    # file  : nan (0.0)
    # http  : 30.0
    # rtsp  : 25.0, 29.97
    fps = vcap.get(cv2.cv.CV_CAP_PROP_FPS)
    fps = vcap.get(5)
    print(fps)

    # camera: -1.0
    # file  : 25.0
    # http  : 14970.0
    # rtsp  : 6203.0, 24572.0
    fps = vcap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
    fps = vcap.get(7)
    print(fps)
