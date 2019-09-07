
# date: 2019.09.04
# https://stackoverflow.com/questions/57791698/how-to-save-an-image-from-a-custom-coco-dataset-with-its-annotations-overlaid-on/57792318#57792318

import skimage.io as io
from PIL import Image, ImageDraw, ImageFont

image = io.imread("https://homepages.cae.wisc.edu/~ece533/images/lena.png")

img = Image.fromarray(image)
draw = ImageDraw.Draw(img)
draw.text((10,10), "Lena", font=ImageFont.truetype("arial", 20), fill=(0,0,0))
img.save('test.png')1
