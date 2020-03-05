#!/usr/bin/env python3

# date: 2020.02.24

import socket
import threading
import sys

# --- functions ---

def recv_msg():
    while True:
        recv_msg = s.recv(1024)
        if not recv_msg:
            sys.exit(0)
        recv_msg = recv_msg.decode()
        print(recv_msg)

def send_msg():
    while True:
        send_msg = input(str("Enter message: "))
        send_msg = send_msg.encode()
        s.send(send_msg)
        print("Message sent")
    
# --- main ---

host = socket.gethostname()
port = 8080

s = socket.socket()
s.connect((host, port))

print("Connected to the server")

message = s.recv(1024)
message = message.decode()
print(message)

# thread has to start before other loop
t = threading.Thread(target=recv_msg)
t.start()

send_msg()

