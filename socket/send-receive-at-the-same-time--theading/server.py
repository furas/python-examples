#!/usr/bin/env python3

# date: 2020.02.24

import socket
import threading
import sys

# --- functions ---

def recv_msg():
    while True:
        recv_msg = conn.recv(1024)
        if not recv_msg:
            sys.exit(0)
        recv_msg = recv_msg.decode()
        print(recv_msg)

def send_msg():
    while True:
        send_msg = input(str("Enter message: "))
        send_msg = send_msg.encode()
        conn.send(send_msg)
        print("message sent")
   
# --- main ---

host = socket.gethostname()
port = 8080

s = socket.socket()
s.bind((host, port))
s.listen(1)

print("Waiting for connections")
conn, addr = s.accept()

print("Client has connected")
conn.send("Welcome to the server".encode())

# thread has to start before other loop
t = threading.Thread(target=recv_msg)
t.start()

send_msg()
