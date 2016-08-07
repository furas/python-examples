from __future__ import print_function
import cv2
import time
import os

# ---------------------------------------------------------------------

# read config data 
with open("config.txt") as conf:
    lines = [line.rstrip() for line in conf]
    time_start_recording = lines[3]
    time_stop_recording = lines[5]
 
# ---------------------------------------------------------------------

# window name
windowname = time.strftime("%Y.%m.%d  %H.%M.%S", time.localtime())

# keys 
KEY_R = ord('r') # start recording
KEY_S = ord('s') # stop recording
KEY_Q = ord('q') # quit

font = cv2.FONT_HERSHEY_PLAIN

# states
running = True 
recording = False
init_recording = False

# other 
video_file_size_end = 1048576 * 200 # split to 50 MB files
fout = 0

# ---------------------------------------------------------------------

# VideoCapture constructor
vcap = cv2.VideoCapture(0) # camera
 
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
 
    # write the next video frame
    if recording:
        if init_recording:
            # VideoWriter constructors
            filename = time.strftime("%Y.%m.%d  %H.%M.%S", time.localtime()) + ".avi"
            fourcc =  cv2.cv.CV_FOURCC('I','4','2','0')
            fout = cv2.VideoWriter(filename, fourcc, fps, (width, height))
            init_recording = False
 
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
        if os.path.getsize(filename) >= video_file_size_end:
            fout.release() # close current file
            init_recording = True # init recording new file
 
        # add REC to frame
        cv2.putText(frame, "REC", (40,40), font, 3 , (0,0,255), 2)
        cv2.circle(frame, (20,20), 10 , (0,0,255), -1)
 
    # add instruction to frame
    cv2.putText(frame,"R - START RECORDING",(width - 200,20), font, 1 ,(255,255,255))
    cv2.putText(frame,"S - STOP RECORDING",(width - 200,40), font, 1 ,(255,255,255))
    cv2.putText(frame,"Q - QUIT",(width - 200,60), font, 1 ,(255,255,255))
 
    # displays an image in the specified window
    cv2.namedWindow(windowname)
    cv2.imshow(windowname, frame)         
 
    # get key (get only lower 8-bits to work with chars)
    key = cv2.waitKey(1) & 0xFF
    
    # check what to do
    if key == KEY_R and not recording:
        print("START RECORDING")
        recording = True
        init_recording = True
    elif key == KEY_S and recording:
        print("STOP RECORDING")
        recording = False
        init_recording = False
        fout.release()
    elif key == KEY_Q:
        print("EXIT")
        running = False
 
#Release everything 
#fout.release()
vcap.release()
cv2.destroyAllWindows()
