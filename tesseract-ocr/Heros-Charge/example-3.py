#!/usr/bin/env python3

from PIL import Image
import pytesseract

'''
Recognize small digits or single digit using option "-psm 6"

$ tesseract.exe -psm 6 image.jpg result.txt
'''

for name in ['number-1.png', 'number-2.jpg', 'number-3.jpg']:
    print('------------------------------')
    print('   filename:', name)
    print('------------------------------')
    
    img = Image.open('screenshots/{}'.format(name))
    
    result = pytesseract.image_to_string(img)
    print('without psm:', result)
    
    result = pytesseract.image_to_string(img, config='-psm 6')#, boxes=True)
    print('   with psm:', result)
    
