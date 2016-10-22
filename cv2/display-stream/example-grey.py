    #!/usr/bin/env python
    
    #
    # rtsp streams: http://wiki.multimedia.cx/index.php?title=RTSP
    #
    
#!/usr/bin/env python

#
# rtsp streams: http://wiki.multimedia.cx/index.php?title=RTSP
#

import cv2

#url = 'video.avi' # local file
#url = 'http://media.dumpert.nl/tablet/9f7c6290_Verstappen_vs._Rosberg_with_Horner_Smile___Streamable.mp4.mp4.mp4'
#url = 'rtsp://granton.ucs.ed.ac.uk/domsdemo/v2003-1.wmv'
#url = 'rtsp://streaming1.osu.edu/media2/ufsap/ufsap.mov'

url = 0 # build-in camera

# open stream
cap = cv2.VideoCapture(url)

# check if opened
if not cap.isOpened():
    print("Can't open file")
else:    
    while True:
        
        # get frame (and status)
        ret, frame = cap.read()

        # exit if no data 
        if not ret:
            break

        # convert to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # display frame
        cv2.imshow('frame', gray)

        # exit if key pressed
        if cv2.waitKey(1) != -1:
            break

# close stream
cap.release()

# close window
cv2.destroyAllWindows()
