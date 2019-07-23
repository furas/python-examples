import cv2
import os

directory = '/home/furas/Obrazy/images/'
upload = cv2.imread("/home/furas/Obrazy/images/ball.png")

for entry in os.listdir(directory):

    if entry.lower().endswith( ('.jpg', '.jpeg', '.png') ):

        fullname = os.path.join(directory, entry)
        #print('fullname:', fullname)
        duplicate = cv2.imread(fullname)

        # it has to check shape to can use (..==..).all() 
        if upload.shape == duplicate.shape and (upload == duplicate).all():
            print("\033[1;32m[v]", entry) # the same 
        else:
            print("\033[1;31m[X]", entry) # different
