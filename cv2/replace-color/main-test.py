import cv2
import numpy as np
import time

# date: 2019.08.06
# https://stackoverflow.com/questions/57372394/how-to-convert-all-white255-255-255-pixels-to-black-0-0-0-using-a-library-fu/57374013#57374013
#
# Replace one color to another: white [255,255,255] to black [0,0,0]
# image: 512x341
#
# if (img[row,col] == [255,255,255]).all():
# time: 2.325188636779785 (seconds)
#
# if all(img[row,col] == [255,255,255]):
# time: 1.5046415328979492 (seconds)
# 
# img[np.where((img==[255,255,255]).all(axis=2))] = [0,0,0]
# time: 0.011182308197021 (seconds)

def version1(img):
    y, x, z = img.shape
    for row in range(y):
        for col in range(x):
            #if all(img[row,col] == [255,255,255]):
            if (img[row,col] == [255,255,255]).all():
                img[row,col] = [0,0,0]
    return img
    
def version2(img):
    y, x, z = img.shape
    for row in range(y):
        for col in range(x):
            if all(img[row,col] == [255,255,255]):
            #if (img[row,col] == [255,255,255]).all():
                img[row,col] = [0,0,0]
    return img
    
def version3(img):
    img[np.where((img==[255,255,255]).all(axis=2))] = [0,0,0]
    return img
    
cv2.namedWindow('window')
img = cv2.imread('/home/furas/Obrazy/images/image.jpg')

start = time.time()
img = version1(img.copy())
end = time.time()
print('time:', end-start)

start = time.time()
img = version2(img.copy())
end = time.time()
print('time:', end-start)

start = time.time()
img = version3(img.copy())
end = time.time()
print('time:', end-start)

cv2.imshow('window', img)
cv2.waitKey()
cv2.destroyAllWindows()

