#!/usr/bin/env python3 

import socket
import threading
import time

# --- functions ---

def client_handler(conn, addr):
    print('connection:', addr[0], addr[1])
    try:
        while True:
            data = conn.recv(100)
            if not data: 
                print('exit:', addr[0], addr[1])
                break
            print(data)
    except Exception as ex:
        print('Exception:', addr[0], addr[1], ex)
    finally:
        print('close:', addr[0], addr[1])
        conn.close()

# --- main ---

port = 23

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('127.0.0.1', port))
print('Telnet opened on port', port)
sk.listen(5)

try:
    while True:
        conn, addr = sk.accept()
        t = threading.Thread(target=client_handler, args=(conn, addr))
        t.start()
except KeyboardInterrupt as ex:
    print('KeyboardInterrupt')
    sk.close()
    print('Telnet closed on port', port)

