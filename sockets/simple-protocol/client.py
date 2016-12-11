#!/usr/bin/env python3

import struct
import socket
import sys

# --- constants ---

HOST = ''   # (local or external) address IP of remote server
PORT = 8000 # (local or external) port of remote server
 
try:
    # --- create socket ---

    print('[DEBUG] create socket')
    
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM

    # --- connect to server ---
    
    print('[DEBUG] connect:', (HOST, PORT))

    s.connect((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

    # --- send data ---

    print('[DEBUG] send')
    
    text = 'Hello World of Sockets in Python'
    print('[DEBUG] text:', text)

    # convert text to bytes
    
    data = text.encode('utf-8')
    print('[DEBUG] data:', data)

    # get data length
    
    length = len(data)
    print('[DEBUG] length:', length)

    # convert `length` int to 4 bytes
    
    length = struct.pack('!i', length)
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
    # --- close socket ---

    print('[DEBUG] close socket')
    
    s.close()
