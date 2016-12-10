#!/usr/bin/env python3

import struct
import socket
import sys

# - constants -

HOST = ''   # (external/local) address IP of remote server
PORT = 8000 # (external/local) port of remote server
 
try:
    # - create socket -
    
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM

    # - connect to server -
    
    s.connect((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

    # - send data -
    
    text = 'Hello World'
    print('[DEBUG] text:', text)

    # convert text to bytes
    
    data = text.encode('utf-8')
    print('[DEBUG] data:', data)

    # get data length
    
    lengt = len(data)
    print('[DEBUG] lengt:', lengt)

    # convert `length` int to 4 bytes
    
    length = struct.pack('!i', lengt)
    print('[DEBUG] length as 4 bytes:', length)

    # send `length` as 4 bytes

    s.send(length)

    # send data as bytes
    
    s.send(data)
    
except Exception as ex:
    print(ex)
except KeyboardInterrupt as ex:
    print(ex)
except:
    print(sys.exc_info())
finally:    
    s.close()
