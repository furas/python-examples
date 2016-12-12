#!/usr/bin/env python3

#
# https://docs.python.org/3.5/library/socket.html
#
 
import socket
import time

# --- constants ---

HOST = ''    # (local or external) address IP of remote server
PORT = 8000  # (local or external) port of remote server

# server can have local address IP - used only in local network
# or external address IP - used in internet on external router
# (and router redirects data to internal address IP)

# --- create socket ---

print('[DEBUG] create socket')

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket() # default value is (socket.AF_INET, socket.SOCK_STREAM)
                    # so you don't have to use it in socket()

# --- connect to server --- 

print('[DEBUG] connect:', HOST, PORT)

s.connect((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

# --- sending receivng many times ---

try:
    while True:

        now = int(time.time())

        # --- send data ---

        # if you don't use native characters
        # then you can use 'ascii' instead of 'utf-8'

        text = "Hello World of Sockets in Python"
        data = text.encode('utf-8') # encode string to bytes
        s.send(data)     

        print('[{}] send: {}'.format(now, text))

        # --- receive data ---

        # if you don't use native characters
        # then you can use 'ascii' instead of 'utf-8'

        data = s.recv(1024)
        text = data.decode('utf-8') # decode bytes to string

        print('[{}] recv: {}'.format(now, text))

        # --- wait awhile ---
        
        time.sleep(1)

except Exception as e:
    print('[DEBUG] exception:', e)

# --- close socket ---
 
print('[DEBUG] close socket')

s.close()
