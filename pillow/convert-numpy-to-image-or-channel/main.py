
# date: 2019.09.07
# https://stackoverflow.com/questions/57830102/how-can-i-save-a-image-converted-from-grayscale-to-rgb-in-python/57830167#57830167

from PIL import Image
import numpy as np

i = Image.open('Obrazy/images/image.jpg')
print('i pixel:', i.getpixel((2,0)))

i = i.convert('L') # convert RGB to grayscale to have only one channel
print('i.size:', i.size)  #(x, y)
print('i pixel:', i.getpixel((2,0)))

# need 'int8' or 'uint8' to correctly convert later to RGB
dim = np.zeros((i.size[1], i.size[0]), 'uint8') #different order (y, x)
print('dim.shape:', dim.shape)

R = np.stack((i, dim, dim), axis=2)
#R = np.stack((i, i, i), axis=2)

print('R.shape;', R.shape)
print('R.dtype:', R.dtype)
print('R pixel:', R[0,2])

img = Image.fromarray(R, 'RGB')
img.save('output-1.jpg')
print('img pixel:', img.getpixel((2, 0)))

# ---------------------------------------

img_zero = Image.fromarray(dim, 'L')

img = Image.merge('RGB', (i, img_zero, img_zero))
img.save('output-2.jpg')
print('img pixel:', img.getpixel((2,0)))

