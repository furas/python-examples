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

# --- functions ---

def get_text(image, region):
    return pytesseract.image_to_string(image.crop(region))

def get_int(image, region):
    return int(get_text(image, region).replace(',', ''))

# --- main ---

# test on screenshots: 0.jpg ... 9.jpg
for x in range(10):
    img = Image.open('screenshots/{}.jpg'.format(x))

    region = (255, 590, 255+210, 590+35)
    text = get_text(img, region)
    print('Name:', text)

    region = (880, 787, 880+170, 787+60)
    value = get_int(img, region)
    print('Power:', value)

    region = (1295, 377, 1295+150, 377+70)
    value = get_int(img, region)
    print('Loot #1:', value)

    region = (1295, 467, 1295+150, 467+70)
    value = get_int(img, region)
    print('Loot #2:', value)

    region = (1295, 557, 1295+150, 557+70)
    value = get_int(img, region)
    print('Loot #3:', value)

    print('-----')


'''
Name: Adrian
Power: 101919
Loot #1: 642
Loot #2: 2686
Loot #3: 737
-----
Name: Phillis
Power: 94744
Loot #1: 2611
Loot #2: 1086
Loot #3: 725
-----
Name: Chanelle
Power: 105950
Loot #1: 2522
Loot #2: 4319
Loot #3: 896
-----
Name: Bettina
Power: 92470
Loot #1: 1558
Loot #2: 4112
Loot #3: 294
-----
Name: Jules
Power: 99594
Loot #1: 1236
Loot #2: 3399
Loot #3: 741
-----
Name: Vina
Power: 100703
Loot #1: 376
Loot #2: 1265
Loot #3: 158
-----
Name: Yannick
Power: 107022
Loot #1: 947
Loot #2: 3890
Loot #3: 597
-----
Name: Phinehas
Power: 102793
Loot #1: 2853
Loot #2: 1086
Loot #3: 610
-----
Name: Nelly
Power: 105936
Loot #1: 3148
Loot #2: 4724
Loot #3: 890
-----
Name: Shauna
Power: 103122
Loot #1: 1627
Loot #2: 4994
Loot #3: 304
-----
'''
