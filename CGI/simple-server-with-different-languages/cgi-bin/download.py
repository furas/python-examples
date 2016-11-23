#!/usr/bin/env python

import os
import sys

fullpath = 'images/normal.png'
filename = 'hello_world.png'

# headers
print 'Content-Type: application/octet-stream; name="%s"' % filename
print 'Content-Disposition: attachment; filename="%s"' % filename
print "Content-Length: " + str(os.stat(fullpath).st_size)
print    # empty line between headers and body
#sys.stdout.flush() # send header faster

try:
    # body
    with open(fullpath, 'rb') as fo: 
        print fo.read()
except Exception as e:
    print 'Content-type:text/html'
    print    # empty line between headers and body
    print 'Exception:', e
