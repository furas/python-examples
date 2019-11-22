#!/usr/bin/env python3

# date: 2019.10.30
# https://stackoverflow.com/questions/58628006/how-to-upload-data-from-memory-via-ftp-in-python-3

from ftplib import FTP
import io

import csv

data = [
    ['Temperature', 0, 0], 
    ['Humidity', 0, 0]
]

bio = io.BytesIO()
iow = io.TextIOWrapper(bio)  # create String wrapper

csv_writer = csv.writer(iow) # create csv writer
csv_writer.writerows(data)   # write all rows

iow.flush()  # force String to send all from buffer to file (you can't use `iow.close()` for it)
bio.seek(0)  # move to beginning of file

ftp.storbinary('STOR data.csv', bio)

ftp = FTP('my_host')
ftp.login('my_login', 'my_password')
ftp.cwd('my_folder')
#ftp.dir()
ftp.storbinary('STOR data.csv', bio)

# to see what is in bio
#bio.seek(0)
#print(bio.read()) 


