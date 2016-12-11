#!/usr/bin/env python3

import struct
import socket
import sys

# --- constants ---

HOST = ''   # local address IP (not external address IP)

            # '0.0.0.0' or '' - conection on all NICs (Network Interface Card),
            # '127.0.0.1' or 'localhost' - local conection only (can't connect from remote computer)
            # 'local_IP' - connection only on one NIC which has this IP
            
PORT = 8000 # local port (not external port)

try:
    # --- create socket ---

    print('[DEBUG] create socket')    

    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = socket.socket() # default value is (socket.AF_INET, socket.SOCK_STREAM) so you don't have to use it

    # --- options ---
     
    # solution for "[Error 89] Address already in use". Use before bind()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # --- assign socket to local IP (local NIC) ---

    print('[DEBUG] bind:', (HOST, PORT))

    s.bind((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

    # --- set size of queue ---

    print('[DEBUG] listen')
     
    s.listen(1) # number of clients waiting in queue for "accept".
                # If queue is full then client can't connect.

    while True:
        # --- accept client ---
        
        # accept client and create new socket `conn` (with different port) for this client only
        # and server will can use `s` to accept other clients (if you will use threading)

        print('[DEBUG] accept ... waiting')
        
        conn, addr = s.accept() # socket, address

        print('[DEBUG] addr:', addr)

        # --- receive data ---

        print('[DEBUG] receive')
        
        # receive length as 4-bytes
        
        length = conn.recv(4)

        print('[DEBUG] length as 4 bytes:', length)

        # convert length from 4-bytes to int

        length = struct.unpack('!i', length)[0] # unpack returns tuple with one element

        print('[DEBUG] length:', length)
        
        # receive data as bytes using length
        
        data = conn.recv(length)

        print('[DEBUG] data:', data)

        # convert bytes to text
        
        text = data.decode('utf-8')

        print('[DEBUG] text:', text)

        # --- close connection ---
        
        # first close `conn`, later `s`
        print('[DEBUG] close conn')

        conn.close()
    
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
