
# date: 2019.09.16

# Use this script to generate image with many faces
# which you can use with `main.py` to detect many faces

import os
import sys
import argparse
import random
from PIL import Image

HOME = os.path.dirname(os.path.realpath(sys.argv[0]))
print('HOME:', HOME)

FOLDER = 'original images'
print('FOLDER:', FOLDER)

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--rows', default=5, help='how many rows with faces [default: 5]')
    parser.add_argument('-c', '--cols', default=5, help='how many columns with faces [default: 5]')
    parser.add_argument('-W', '--width', default=640, help='width of every imagew with face [default: 640]')
    parser.add_argument('-H', '--height', default=480, help='height of every imagew with face [default: 480]')
    parser.add_argument('-o', '--output', default='generated.png', help='name of output image [default: generated.png]')
    args = parser.parse_args()

    return args

def generate(args):

    # get names of all images with faces
    names = list(os.listdir(os.path.join(HOME, FOLDER)))
    print('images:', len(names))

    # get random faces to create image
    selected = random.choices(names, k=args.rows*args.cols)
    print('selected:', len(selected))

    # create empty image for faces
    output_img = Image.new('RGB', (args.width*args.cols, args.height*args.rows))

    # put faces on image
    it = iter(selected)
    for y in range(0, args.height*args.rows, args.height):
        for x in range(0, args.width*args.cols, args.width):
            path = os.path.join(FOLDER, next(it))
            img = Image.open(path)
            img = img.resize((args.width, args.height))
            output_img.paste(img, (x, y))

    # save image
    output_img.save(args.output)
    print('size:', output_img.size)

def main():
    args = get_arguments()
    generate(args)

if __name__ == '__main__':
    main()
