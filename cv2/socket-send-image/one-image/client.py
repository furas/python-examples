import socket
import cv2 
import pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4000))

serialized_img = b''

while True:
    packet = client_socket.recv(1024)
    if not packet :
        break
    serialized_img += packet

img = pickle.loads(serialized_img)

cv2.imshow('client', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

