#!/usr/bin/env python3 

import cv2
import numpy 

image = cv2.imSread('Obrazy/images/image.jpg', 1)

image = numpy.array([list(reversed(row)) for row in image])

cv2.imshow('window', image)

cv2.waitKey(0)
