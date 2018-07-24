#!/usr/bin/env python

#
# rtsp links: http://wiki.multimedia.cx/index.php?title=RTSP
#

import cv2

# --- local file ---
#stream = 'video.avi'

# --- http stream ---
# doesn't work any more
#stream = 'http://media.dumpert.nl/tablet/9f7c6290_Verstappen_vs._Rosberg_with_Horner_Smile___Streamable.mp4.mp4.mp4'

# --- rtsp stream ---
# doesn't work any more
#stream = 'rtsp://granton.ucs.ed.ac.uk/domsdemo/v2003-1.wmv'

stream = 'rtsp://streaming1.osu.edu/media2/ufsap/ufsap.mov'

# --- local (build-in) camera ---
#stream = 0


# --- main ---

# open stream
cap = cv2.VideoCapture(stream)

if not cap.isOpened():
    print("Can't open stream/file")
else:    
    while True:
        # read one frame (and "return" status)
        ret, frame = cap.read()

        # exit if error
        if not ret:
            break

        # (open window and) display one frame
        cv2.imshow('frame', frame)

        # exit if pressed any key
        # (it doesn't wait for key so you can read next frame)
        # (you have to one window to catch pressed key)
        if cv2.waitKey(1) != -1:
            break

# close stream
cap.release()

# close window
cv2.destroyAllWindows()
