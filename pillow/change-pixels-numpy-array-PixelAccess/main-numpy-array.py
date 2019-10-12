#!/usr/bin/env python3

# date: 2019.09.29

# it converts `Image` to numpy array
# so it has to convert it back to `Image`

# BTW: array  uses [row,col] instead of [col,row]

from PIL import Image
import numpy as np

img1 = Image.open('Obrazy/images/image.jpg')

pixels = np.array(img1)

pixels[np.all(pixels == (0, 0 ,0), axis=-1)] = (255,0,0)

img2 = Image.fromarray(pixels)
img2.show()


