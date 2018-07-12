#!/usr/bin/env python3

#
# you can test with `netcat` as client with `-u` for UDP
#
# $ nc -u localhost 3000 
#

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 3000))

while True:
    data, address = s.recvfrom(1024)
    print(data.decode('ascii'), end='')
    s.sendto(data, address)
