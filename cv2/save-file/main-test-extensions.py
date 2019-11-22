import cv2

# http://www.fourcc.org/codecs.php
cam = cv2.VideoCapture(0)

print(' width:', int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('height:', int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))

SIZE = (320, 240)

codecs = (  # MP4, AVI,
    'I420', #  - ,  + ,
    'MP4V', #  - ,  - ,
    'MP42', #  - ,  + ,
    'AVC1', #  - ,  - , 
    'H264', #  - ,  ? ,
    'WRAW', #  - ,  - ,
    'MPEG', #  - ,  + , 
    'MJPG', #  - ,  + ,
    'XVID', #  - ,  + ,
    'H265', #  ? ,  ? ,
    'X264', #  - ,  ? ,
)

for cc in codecs:
    print('\n\n')
    for ext in ('mkv', 'mpeg', 'mp4', 'avi'):
        print('---', cc, '/', ext, '---')
        fourcc = cv2.VideoWriter_fourcc(*cc)
        out = cv2.VideoWriter('output.' + ext, fourcc, 15, SIZE)
        out.release()

