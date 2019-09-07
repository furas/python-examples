#!/usr/bin/env python

# date: 2019.09.02
# https://stackoverflow.com/questions/57755712/how-do-i-resolve-contract-object-has-no-attribute-filter-in-pil-imageenhanc/57756236#57756236

from PIL import Image
from PIL import ImageEnhance

image = Image.open("old_image.jpg")

enhancer = ImageEnhance.Contrast(image)
new_image = enhancer.enhance(1.5)

new_image.save("new_image.jpg")
