#
# https://docs.python.org/3.5/library/socket.html
#
 
# --- CLIENT ---
 
#!/usr/bin/env python3
 
import socket

# - constants -
 
HOST = ''    # (external/local) address IP of remote server
PORT = 8000  # (external/local) port of remote server

# server can have internal/local address IP - used only in local network
# or external address IP - used in internet on external router
# (and router redirects data to internal address IP)

# - create socket -
 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket() # default value is (socket.AF_INET, socket.SOCK_STREAM) so you don't have to use it

# - connect to server - 

s.connect((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

# - send/receive data -

s.send("Hello".encode('utf-8'))     # encode string to bytes

print(s.recv(1024).decode('utf-8')) # decode bytes to string

# - close socket -
 
s.close()
