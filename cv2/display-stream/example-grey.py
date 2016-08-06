#!/usr/bin/env python

#
# rtsp streams: http://wiki.multimedia.cx/index.php?title=RTSP
#

import cv2

#url = 'video.avi'
url = 'http://media.dumpert.nl/tablet/9f7c6290_Verstappen_vs._Rosberg_with_Horner_Smile___Streamable.mp4.mp4.mp4'
url = 'rtsp://granton.ucs.ed.ac.uk/domsdemo/v2003-1.wmv'
#url = 'rtsp://streaming1.osu.edu/media2/ufsap/ufsap.mov'

cap = cv2.VideoCapture(url)


if not cap.isOpened():
    print "Can't open file"
else:    
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # convert to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)

        if cv2.waitKey(1) != -1:
            break

cap.release()
cv2.destroyAllWindows()
