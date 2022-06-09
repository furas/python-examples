# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.06.07
#
# [python - Stream OpenCV Video Capture to flask server - Stack Overflow](https://stackoverflow.com/questions/72522805/stream-opencv-video-capture-to-flask-server/)
#
# https://blog.miguelgrinberg.com/post/video-streaming-with-flask

#
# Send stream from webcam to flask
#

import requests
import cv2
import time

cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()

    if success:
        cv2.imshow("OUTPUT", img)

        _, imdata = cv2.imencode('.JPG', img)

        print('.', end='', flush=True)

        requests.put('http://127.0.0.1:5000/upload', data=imdata.tobytes())

    # 40ms = 25 frames per second (1000ms/40ms),
    # 1000ms = 1 frame per second (1000ms/1000ms)
    # but this will work only when `imshow()` is used.
    # Without `imshow()` it will need `time.sleep(0.04)` or `time.sleep(1)` to slow down

    if cv2.waitKey(40) == 27:  # 40ms = 25 frames per second (1000ms/40ms)
        break

    #time.sleep(1) # for test slow down to 1fps

cv2.destroyAllWindows()
cap.release()

