#!/usr/bin/env python3

#
# https://docs.python.org/3.5/library/socket.html
#
 
import socket
import threading
import time

# --- constants ---
 
HOST = ''   # local address IP (not external address IP)

            # '0.0.0.0' or '' - conection on all NICs (Network Interface Card),
            # '127.0.0.1' or 'localhost' - local conection only (can't connect from remote computer)
            # 'local_IP' - connection only on one NIC which has this IP
            
PORT = 8000 # local port (not external port)


# --- functions ---

def handle_client(conn, addr):

    try:
        while True:
            # --- receive/send data ---

            # if client first `send()` and next `recv()`
            # then server have to first `recv`() and next `send()`

            # if both will `recv()` at the same time then all will hang
            # because both will wait for data and nobody will `send()`

            # if you don't use native characters
            # then you can use 'ascii' instead of 'utf-8'

            now = int(time.time())

            # receiving
            
            data = conn.recv(1024)
            text = data.decode('utf-8') # decode bytes to string

            print('[{}][{}] recv: {}'.format(addr, now, text))

            # sending
            
            text = 'Thank you [{}]'.format(now)
            data = text.encode('utf-8') # encode string to bytes
            conn.send(data)

            print('[{}]][{}] send: {}'.format(addr, now, text))
            
    except Exception as e:
        print('[DEBUG] exception:', e)
    
# --- create socket ---

print('[DEBUG] create socket')

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket() # default value is (socket.AF_INET, socket.SOCK_STREAM)
                    # so you don't have to use it in socket()

# --- options ---
 
print('[DEBUG] set options')

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

    conn, addr = s.accept()

    print('[DEBUG] addr:', addr)

    # --- run thread ---

    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()
    
# --- close all sockets ---
 
# alway first close `conn`, next close `s`

print('[DEBUG] close socket(s)')

conn.close()
s.close()
