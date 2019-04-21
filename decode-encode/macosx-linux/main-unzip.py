
# date: 2019.04.18
# Bartlomiej 'furas' Burek
#
# https://stackoverflow.com/questions/16467479/normalizing-unicode
#
#

import os
import zipfile
import unicodedata
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='zip file with MAC OS X names')
args = parser.parse_args()

def convert(name):
    name = name.encode('cp437').decode('utf-8')
    name = unicodedata.normalize('NFC', name)
    return name

if args.filename:
    z = zipfile.ZipFile(args.filename)
    for item in z.filelist:
        #if not item.filename.startswith('__MACOSX'):
        new_name = convert(item.filename)
        print(new_name)
        if item.is_dir():
            os.makedirs(new_name, exist_ok=True)
        else:
            with open(new_name, 'wb') as f:
                f.write(z.read(item))


