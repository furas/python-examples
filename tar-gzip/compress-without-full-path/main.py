#!/usr/bin/env python3 

# date: 2019.12.14

import os
import tarfile

folder = 'Obrazy/images'
filename = 'image-800x600.jpg'
path = os.path.join(folder, filename)

output = path + '.tar.gz'

t = tarfile.open(output, mode='w:gz')
t.add(path, filename)

t.close()
