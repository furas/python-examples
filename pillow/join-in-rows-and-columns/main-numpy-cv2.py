#!/usr/bin/env python3 

# date: 2019.11.26
# 

import cv2
import numpy as np

img1 = cv2.imread('square-1.png')
img2 = cv2.imread('square-2.png')
img3 = cv2.imread('square-3.png')
img4 = cv2.imread('square-4.png')

row1 = np.concatenate((img1, img2), axis=1)
row2 = np.concatenate((img3, img4), axis=1)
new_image = np.concatenate((row1, row2))

row1 = np.hstack((img1, img2))
row2 = np.hstack((img3, img4))
new_image = np.vstack((row1, row2))

cv2.imwrite('new.png', new_image)



