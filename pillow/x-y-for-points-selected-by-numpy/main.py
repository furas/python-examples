#!/usr/bin/env python3

from PIL import Image
import numpy as np

img = Image.open('image.png')

img = img.convert('L')
arr = np.array(img)

data = np.where(arr > 200)

points_y_x = list(zip(*data))
points_x_y = list(zip(data[1], data[0]))

print(points_y_x)
print(points_x_y)

