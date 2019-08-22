import numpy as np
import csv
from PIL import Image

counter = dict()

row = [
        128, 255, 128,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 128, 255, 128,
          0,   0,   0, 128, 255, 128, 128, 255, 128, 128, 255, 128, 128, 255, 128, 128, 255, 128,   0,   0,   0,
          0,   0,   0, 128, 255, 128,   0,   0,   0, 128, 255, 128,   0,   0,   0, 128, 255, 128,   0,   0,   0,
          0,   0,   0, 128, 255, 128, 128, 255, 128, 128, 255, 128, 128, 255, 128, 128, 255, 128,   0,   0,   0,
          0,   0,   0, 128, 255, 128,   0,   0,   0,   0,   0,   0,   0,   0,   0, 128, 255, 128,   0,   0,   0,
          0,   0,   0, 128, 255, 128, 128, 255, 128, 128, 255, 128, 128, 255, 128, 128, 255, 128,   0,   0,   0,
        128, 255, 128,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 128, 255, 128,
        'face'
      ]

pixels = row[:-1]

pixels = np.array(pixels, dtype='uint8')
pixels = pixels.reshape((7, 7, 3))
image = Image.fromarray(pixels)

label = row[-1]

if label not in counter:
    counter[label] = 0
counter[label] += 1

filename = '{}{}.png'.format(label, counter[label])

image.save(filename)

print('saved:', filename)
