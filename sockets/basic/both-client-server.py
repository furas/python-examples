#
# https://docs.python.org/3.5/library/socket.html
#
 
# --- CLIENT ---
 
#!/usr/bin/env python3
 
import socket
 
HOST = ''
PORT = 8000
 
s = socket.socket()
 
s.connect((HOST, PORT))
 
s.send("Hello".decode('utf-8'))
print(s.recv(1024).encode('utf-8'))
 
s.close()
