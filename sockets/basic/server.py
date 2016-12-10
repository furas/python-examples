#
# https://docs.python.org/3.5/library/socket.html
#
 
# --- SERVER ---
 
#!/usr/bin/env python3
 
import socket
import time
 
HOST = ''   # local address IP (not external address IP)

# '0.0.0.0' or '' - conection on all NICs (Network Interface Card),
# '127.0.0.1' or 'localhost' - local conection only (can't connect from remote computer)
# 'local_IP' - connection only on one NIC which has this IP
            
PORT = 8000 # local port (not external port)

s = socket.socket() # default is (socket.AF_INET, socket.SOCK_STREAM) so you don't have to use it
 
# solution for "[Error 89] Address already in use". Use before bind()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
s.bind((HOST, PORT)) # one tuple (HOST, PORT), not two arguments
s.listen(1)          # number of clients waiting in queue for "accept". If queue is full then client can't connect.
 
try:
    # client can wait for accept()
    # but can't wait for bind() and listen()
 
    print('[DEBUG] sleep ... for test only (normally you don\'t need it)')    
    time.sleep(5)  # waiting for test only (normally you don\'t need it)
   
    # it creates new socket `conn` to communicate with current client.
    # Server can use `s` to accept next client - if you use thread to communicate with current client.
    print('[DEBUG] accept ...')
    conn, addr = s.accept()
    print('[DEBUG] addr:', addr)
 
    print(conn.recv(1024).encode('utf-8')) # decode bytes to string
    conn.send('World'.decode('utf-8'))     # encode string to bytes
   
except Exception as e:
    print(e)
 
# alway first close `conn`, next close `s`
conn.close()
s.close()
