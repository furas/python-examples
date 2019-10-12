#!/usr/bin/env python3

# date: 2019.09.29

# `PixelAccess` changes pixels in original `img` 
# so there is no need to convert it back to `Image`

# BTW: Image uses [col,row] (array uses [row,col])

from PIL import Image

img = Image.open('image.jpg')

pixels = img.load()

width, height = img.size
for col in range(width):
    for row in range(height):
        if pixels[col,row] == (0, 0, 0):
            pixels[col,row] = (255, 0 ,0)

img.show()
