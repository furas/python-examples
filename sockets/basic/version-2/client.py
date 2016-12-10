#!/usr/bin/env python3

#
# https://docs.python.org/3.5/library/socket.html
#
 
import socket
 
# - constants -

HOST = ''    # (local or external) address IP of remote server
PORT = 8000  # (local or external) port of remote server

# server can have local address IP - used only in local network
# or external address IP - used in internet on external router
# (and router redirects data to internal address IP)

SIZE = 10    # size of received parts of message

# - create socket -
 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket() # default value is (socket.AF_INET, socket.SOCK_STREAM) so you don't have to use it

# - connect to server - 

s.connect((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

# - send/receive data -

# sending data
   
text = "Hello World of Sockets in Python"
data = text.encode('utf-8') # encode string to bytes
s.send(data)

# receiving longer data using small buffer

data = b'' # empty byte 

while True:
    part = s.recv(SIZE)
    print('[TEST] part:', part)
    data += part

    if len(part) < SIZE:
        break

text = data.decode('utf-8') # decode bytes to string

print(text)

# - close socket -
 
s.close()
