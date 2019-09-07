
# date: 2019.09.04
# https://stackoverflow.com/questions/57791698/how-to-save-an-image-from-a-custom-coco-dataset-with-its-annotations-overlaid-on/57792318#57792318

import skimage.io as io
import matplotlib.pyplot as plt

image = io.imread("https://homepages.cae.wisc.edu/~ece533/images/lena.png")

plt.imshow(image)
plt.axis('off')
plt.annotate("Lena", (10, 20))
plt.savefig("output.png", bbox_inches='tight', pad_inches=0)

