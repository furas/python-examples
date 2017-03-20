#!/usr/bin/env python3

#
# Linux (Debian/Ubuntu/Mint) install:
#
#   apt install tesseract-ocr
#
# Python install:
#
#   pip install pillow
#   pip install pytesseract
#
# Links:
#   tesseract-ocr: https://github.com/tesseract-ocr/tesseract/wiki
#   pytesseract: https://github.com/madmaze/pytesseract
#   pillow: http://pillow.readthedocs.io
#

from PIL import Image
import pytesseract
#import PIL.ImageOps

region_power = (880, 787, 880+170, 787+60)

# find value on screenshots 0.jpg ... 9.jpg
for x in range(10):
    # open image
    img = Image.open('screenshots/{}.jpg'.format(x))

    # get region
    img = img.crop(region_power)

    # above code in one line
    #img = Image.open('{}.jpg'.format(x)).crop(region_power)

    # invert colors - to get dark text on light background
    #img = PIL.ImageOps.invert(img)

    # convert to grayscale
    #img = img.convert('L')

    # above code in one line
    #img = PIL.ImageOps.invert(img).convert('L')

    # save region in file to see what was cropped
    #img.save('region-{}.jpg'.format(x))

    result = pytesseract.image_to_string(img)

    print('Power:', result)
