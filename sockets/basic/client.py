#
# https://docs.python.org/3.5/library/socket.html
#
 
# --- CLIENT ---
 
#!/usr/bin/env python3
 
import socket
 
HOST = ''    # (external) address IP of remote server
PORT = 8000  # (external) port of remote server
 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket() # default value is (socket.AF_INET, socket.SOCK_STREAM) so you don't have to use it
 
s.connect((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

s.send("Hello".encode('utf-8'))     # encode string to bytes

print(s.recv(1024).decode('utf-8')) # decode bytes to string
 
s.close()
