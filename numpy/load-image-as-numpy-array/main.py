import numpy as np
import matplotlib.pyplot as plt

filename = 'Obrazy/images/image.jpg'

# ---

import matplotlib.pyplot

img = matplotlib.pyplot.imread(filename)

print(type(img), img.shape)

plt.imshow(img)
plt.show()

# ---

import cv2

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(type(img), img.shape)

plt.imshow(img)
plt.show()

# ---

import imageio

img = np.array(imageio.imread(filename))
img = np.array(img)

print(type(img), img.shape)

plt.imshow(img)
plt.show()

# ---

import PIL.Image

img = PIL.Image.open(filename)
img = np.array(img)

print(type(img), img.shape)

plt.imshow(img)
plt.show()

# ---

import pygame

img = pygame.image.load(filename)
img = pygame.surfarray.array3d(img)
img = img.swapaxes(0,1)

print('pygame:', type(img), img.shape)

plt.imshow(img)
plt.show()

# ---

import skimage

#img = skimage

#print(type(img), img.shape)

#plt.imshow(img)
#plt.show()

---

import scipy.misc

img = scipy.misc.imread(filename)

print('scipy:', type(img), img.shape)

plt.imshow(img)
plt.show()

#DeprecationWarning: `imread` is deprecated!
#`imread` is deprecated in SciPy 1.0.0, and will be removed in 1.2.0.
#Use ``imageio.imread`` instead.

# ---

from keras.preprocessing.image import load_img

img = load_img(filename)

print('keras:', type(img))#, img.shape)

plt.imshow(img)
plt.show()



