#!/usr/bin/env python3

'''Display data send as gzip'''

import urllib
import gzip
import io 

url = 'http://www.stream-urls.de/webradio'

r  = urllib.urlopen(url)

# create file-like object in memory
buf = io.StringIO(r.read())

# create gzip object using file-like object instead of real file on disk
f = gzip.GzipFile(fileobj=buf)

# get data from file
html = f.read()

print('---')

print(r.text[:250], '...')


#print('Content-Type     :', r.headers['Content-Type'])
#print('Content-Encoding :', r.headers['Content-Encoding'])


