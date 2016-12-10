#
# https://docs.python.org/3.5/library/socket.html
#
 
# --- SERVER ---
 
#!/usr/bin/env python3
 
import socket
import time
 
# - constants -

HOST = ''   # local address IP (not external address IP)

            # '0.0.0.0' or '' - conection on all NICs (Network Interface Card),
            # '127.0.0.1' or 'localhost' - local conection only (can't connect from remote computer)
            # 'local_IP' - connection only on one NIC which has this IP
            
PORT = 8000 # local port (not external port)

# - create socket -

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket() # default value is (socket.AF_INET, socket.SOCK_STREAM) so you don't have to use it

# - options -
 
# solution for "[Error 89] Address already in use". Use before bind()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# - assign socket to local IP (local NIC)  -

s.bind((HOST, PORT)) # one tuple (HOST, PORT), not two arguments

# - set size of queue -
 
s.listen(1)          # number of clients waiting in queue for "accept". If queue is full then client can't connect.
 
try:
    # - for test only - you don't need it -
    
    # client can wait for accept()
    # but can't wait for bind() and listen()
 
    print('[DEBUG] sleep ... for test only (normally you don\'t need it)')    
    time.sleep(5)  # waiting for test only (normally you don\'t need it)

    # - accecpt client -
     
    # accept client and create new socket `conn` (with different port) for this client only
    # and server will can use `s` to accept other clients (if you will use threading)
        
    print('[DEBUG] accept ...')
    conn, addr = s.accept()
    print('[DEBUG] addr:', addr)

    # - recevier/send data -

    # if client first `send()` and next `recv()`
    # then server have to first `recv`() and next `send()`
    #
    # if both will `recv()` at the same time then all will hang
    # because both will wait for data and nobody will `send()`
   
    print(conn.recv(1024).encode('utf-8')) # decode bytes to string

    conn.send('World'.decode('utf-8'))     # encode string to bytes
   
except Exception as e:
    print(e)

# - close all sockets -
 
# alway first close `conn`, next close `s`
conn.close()
s.close()



# --- CLIENT ---
 
#!/usr/bin/env python3
 
import socket
 
HOST = ''    # (external/local) address IP of remote server
PORT = 8000  # (external/local) port of remote server

# server can have local address IP - used only in local network
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
