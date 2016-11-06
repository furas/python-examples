#!/usr/bin/env python3

import sys
import os

src =  "images/normal.png"

sys.stdout.write("Content-Type: image/png\n")
sys.stdout.write("Content-Length: " + str(os.stat(src).st_size) + "\n")
sys.stdout.write("\n")
sys.stdout.flush()
sys.stdout.buffer.write(open(src, "rb").read())

