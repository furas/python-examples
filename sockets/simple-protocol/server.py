#!/usr/bin/env python3

import struct
import socket
import sys

# --- constants ---

HOST = ''   # '0.0.0.0' or '' - for conection on all NIC (Network Interface Card),
            # '127.0.0.1' or 'localhost' - for local conection only (no remote access)
            # 'local_IP' - for conection on one NIC - which have local_IP address
PORT = 8000

try:
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM

    # solution for "[Error 89] Address already in use", use before bind()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
    s.bind((HOST, PORT)) # tuple
    s.listen(1)          # number of clients waiting in queue

    while True:
        sx, ax = s.accept() # socket, address
    
        print('[DEBUG] conn:', ax)

        # receive data length
        x = sx.recv(4)
        print('[DEBUG] x:', x)

        length = struct.unpack('!i', x)[0] # it returns tuple with one element
        print('[DEBUG] length:', length)
        
        # receive data
        data = sx.recv(length)
        print('[DEBUG] data:', data)

        # convert bytes to text
        text = data.decode('utf-8')
        print('[DEBUG] text:', text)

        # first close `conn`, later `sock`
        sx.close()
    
except Exception as ex:
    print(ex)
except KeyboardInterrupt as ex:
    print(ex)
except:
    print(sys.exc_info())
finally:
    s.close()
