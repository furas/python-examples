#!/usr/bin/env python2

'''Display data send as gzip'''

import urllib
import gzip
import io

url = 'http://www.stream-urls.de/webradio'

r = urllib.urlopen(url)

print('--- HEADERS ---')

print 'Content-Type     :', r.headers['Content-Type']      # gzip
print 'Content-Encoding :', r.headers['Content-Encoding']  # text/html; charset=utf-8

print '--- HTML ---'

# create file-like object in memory
buf = io.BytesIO(r.read())

# create gzip object using file-like object instead of real file on disk
f = gzip.GzipFile(fileobj=buf)

# get data from file
html = f.read().decode('utf-8')


print html[:250], '...'


