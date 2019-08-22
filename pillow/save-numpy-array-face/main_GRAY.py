import numpy as np
import csv
from PIL import Image

counter = dict()

row = [
        255,   0,   0,   0,   0,   0,  255,
          0, 255, 255, 255, 255, 255,    0,
          0, 255,   0, 255,   0, 255,    0,
          0, 255, 255, 255, 255, 255,    0,
          0, 255,   0,   0,   0, 255,    0,
          0, 255, 255, 255, 255, 255,    0,
        255,   0,   0,   0,   0,   0,  255,
        'face'
      ]

pixels = row[:-1]

pixels = np.array(pixels, dtype='uint8')
pixels = pixels.reshape((7, 7))

image = Image.fromarray(pixels)
image.show()

label = row[-1]

if label not in counter:
    counter[label] = 0
counter[label] += 1

filename = '{}{}.png'.format(label, counter[label])
image.save(filename)
         
print('saved:', filename)
