#!/usr/bin/env python3

import urllib.request
import io
import gzip

url = 'http://httpbin.org/gzip'

r = urllib.request.urlopen(url)

bytes_compressed = r.read()

mem_file = io.BytesIO(bytes_compressed)

gzip_file = gzip.GzipFile(fileobj=mem_file)

bytes_uncompressed = gzip_file.read()

print(bytes_uncompressed.decode('utf-8'))
