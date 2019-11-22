import cv2

cam = cv2.VideoCapture(0)

print(' width:', int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('height:', int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))

SIZE = (320, 240)

for ext in ('mp4', 'avi'):
#    print('---', ext, '---')
    for cc in ('I420', 'MP4V', 'MP42', 'AVC1', 'H264', 'WRAW', 'MPEG', 'MJPG', 'XVID', 'H265'):
        print('---', ext, '---', cc, '---')
        fourcc = cv2.VideoWriter_fourcc(*cc)
        out = cv2.VideoWriter('output.' + ext, fourcc, 15, SIZE)
        out.release()
# DIVX needs extension .avi
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 15, SIZE)

for x in range(100):
    ret, frame = cam.read()

    # if `cam.get()` gives `(width, height)` different than `SIZE`
    # then `frame` has to be resized before writing in file
    frame = cv2.resize(frame, SIZE) 
    
    out.write(frame)
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(10)
    if key & 0xff == 27: # ESC
        break
    
out.release()
cv2.destroyAllWindows()
