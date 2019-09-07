
# date: 2019.08.26
# To test cron settings
# * * * * * /usr/bin/python /home/user/script.py > /tmp/output.log

import os
import sys
import datetime

print('Date:', datetime.datetime.now().strftime('%Y.%m.%d'))
print('Time:', datetime.datetime.now().strftime('%H:%M:%S'))
print('Current Working Directory:', os.getcwd())
print('User ID:', os.getuid())

str_user_id = str(os.getuid())

with open('/etc/passwd') as fp:
    for line in fp:
        line = line.rstrip('\n')
        items = line.split(':')
        if items[2] == str_user_id:
            print(' passwd:', line)
            print('   name:', items[0])
            print('   home:', items[5])
            print('  shell:', items[6])
            break
                       
