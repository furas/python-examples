#!/usr/bin/env python3

# date: 2019.09.24
# https://stackoverflow.com/questions/58085439/opencv-extract-pixels-with-rbg/

# replaca pixel when `R > G > B`

import cv2
import numpy as np

img = cv2.imread('/home/furas/Obrazy/images/image.png')

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img[ (img[:,:,2] > img[:,:,1]) & (img[:,:,1] > img[:,:,0]) ] = 0

cv2.imshow('image', img)

cv2.waitKey(0)
