#!/usr/bin/env python3

# date: 2019.10.30
# https://stackoverflow.com/questions/58628006/how-to-upload-data-from-memory-via-ftp-in-python-3

from ftplib import FTP
import io

import json

data = [['Temperature', 0, 0], ['Humidity', 0, 0]]
text = json.dumps(data)

bio = io.BytesIO()
bio.write(text.encode())
bio.seek(0)  # move to beginning of file

ftp = FTP('my_host')
ftp.login('my_login', 'my_password')
ftp.cwd('my_folder')
#ftp.dir()
ftp.storbinary('STOR data.json', bio)

# to see what is in bio
#bio.seek(0)
#print(bio.read()) 

