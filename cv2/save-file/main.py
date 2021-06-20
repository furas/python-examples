import cv2

# --- functions ---

def test_combinations():
    """Test which combinations will work."""
    
    SIZE = (640, 480)
    
    for ext in ('avi', 'mov', 'mp4', 'mkv'):
        for cc in ('I420', 'MP4V', 'MP42', 'AVC1', 'H264', 'WRAW', 'MPEG', 'MJPG', 'XVID', 'H265'):
            print('---', ext, '---', cc, '---')
            
            fourcc = cv2.VideoWriter_fourcc(*cc)
            out = cv2.VideoWriter('output.' + ext, fourcc, 25, SIZE)
            out.release()
        
# --- main ---

cam = cv2.VideoCapture(0)

input_width  = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
input_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

print('input width :', input_width)
print('input height:', input_height)

output_width  = 320
output_height = 240

print('output width :', output_width)
print('output height:', output_height)

input_size  = (input_width, input_height)
output_size = (output_width, output_height)

#test_combinations()

# DIVX needs extension .avi
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 25, output_size)  # 25 FPS 

while True:
#for x in range(100):  # for test write only 100 frames
    ret, frame = cam.read()

    # if `cam.get()` gives `(width, height)` different than `output_size`
    # then `frame` has to be resized before writing in file
    if input_size != output_size:
        frame = cv2.resize(frame, output_size) 
    
    out.write(frame)
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(50)  # 50ms = 1s/25FPS (1000ms/25FPS)
    if key & 0xff == 27: # ESC
        break
    
out.release()
cv2.destroyAllWindows()
