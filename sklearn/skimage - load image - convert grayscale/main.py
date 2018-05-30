import skimage.io
import skimage.color
import matplotlib.pyplot as plt

filename = 'domestic-animals/cat.png'

img = skimage.io.imread(filename)
img_grey = skimage.color.rgb2gray(img)

print(img.shape)
print(img_grey.shape)

plt.imshow(img)
plt.show()

plt.gray()

plt.imshow(img_grey)
plt.show()
