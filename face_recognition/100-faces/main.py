#!/usr/bin/env python3

# date: 2019.09.16
#

# Use `generate_image.py to generate image with many faces
# which you can use with this script to detect many faces

import os
import argparse
import face_recognition
from PIL import Image, ImageDraw


#HOME = os.path.dirname(os.path.realpath(sys.argv[0]))
#print('HOME:', HOME)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default='generated.png', help='name of input image [default: generated.png]')
    parser.add_argument('-o', '--output', default='detected.png', help='name of output image [default: detected.png]')
    args = parser.parse_args()

    return args

def detect(args):
    arr = face_recognition.load_image_file(args.input)
    face_locations = face_recognition.face_locations(arr)
    print('found:', len(face_locations))

    img = Image.open(args.input)
    
    draw = ImageDraw.Draw(img)
    for item in face_locations:
        # array uses (row,column) which means (y,x) but I need (x,y)
        item = item[1], item[0], item[3], item[2]
        draw.rectangle(item, width=3)

    img.save(args.output)

def main():
    args = get_arguments()
    detect(args)

if __name__ == '__main__':
    main()
