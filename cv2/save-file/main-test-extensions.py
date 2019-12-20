#!/usr/bin/env python3 

# date: 2019.12.09 (update)
#
# $ ffmpeg -codecs
# $ ffmpeg -formats
#

import cv2

codecs = (       # MP4, AVI,
#    'I420',      #  - ,  + ,
    'MP4V',      #  - ,  - ,
    'mp4v',      #  + ,  - ,
    'MP42',      #  - ,  + ,
#    'AVC1',      #  - ,  - , 
#    'H264',      #  - ,  ? ,
#    'WRAW',      #  - ,  - ,
    'MPEG',      #  - ,  + , 
    'mpeg',      #  - ,  + , 
#    'MJPG',      #  - ,  + ,
#    'XVID',      #  - ,  + ,
#    'H265',      #  ? ,  ? ,
    'X264',      #  - ,  ? ,
    'x264',      #  - ,  ? ,
    'X265',      #  - ,  ? ,
    'x265',      #  - ,  ? ,
    0x7634706d,  #  + ,  ? , # mp4v - https://stackoverflow.com/a/52839553/1832058
)

extensions = [ # container
#    'mkv', 
#    'mpeg', 
#    'mp4', 
#    'avi', 
#    'mp4v',
    'm4v',    
]


# http://www.fourcc.org/codecs.php
cap = cv2.VideoCapture(0) # built-in camera
#cap = cv2.VideoCapture('video.avi') 

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(' width:', width)
print('height:', height)

# it has to use original size of image. It will not save if SIZE is different.
SIZE = (width, height)

for cc in codecs:
    print('\n\n')
    for ext in extensions:
        print('---', cc, '/', ext, '---')
        if isinstance(cc, str):
            fourcc = cv2.VideoWriter_fourcc(*cc)
        else:
            fourcc = cc
        out = cv2.VideoWriter('output-{}.{}'.format(cc, ext), fourcc, 15, SIZE)
        ret, frame = cap.read()
        out.write(frame)
        out.release()

