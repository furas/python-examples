#!/usr/bin/env python3

import struct
import socket
import sys

address = ('localhost', 8000)

try:
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM
    s.connect(address)

    text = 'Hello World'
    print('[DEBUG] text:', text)

    # convert unicode to bytes
    data = text.encode('utf-8')
    print('[DEBUG] data:', data)

    # send length as 4 bytes
    x = len(data)
    print('[DEBUG] x:', x)
    
    length = struct.pack('!i', x)
    print('[DEBUG] length:', length)

    s.send(length)

    # send data
    s.send(data)
    
except Exception as ex:
    print(ex)
except KeyboardInterrupt as ex:
    print(ex)
except:
    print(sys.exc_info())
finally:    
    s.close()
