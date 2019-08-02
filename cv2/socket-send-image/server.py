import socket
import cv2
import pickle

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 4000))

cap = cv2.VideoCapture(0)
ret, img = cap.read()
cap.release()

if not ret:
    print('exit: no image')
    exit(1)
    
cv2.imshow('server', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

serialized_img = pickle.dumps(img)

while ret:
    try:
        server_socket.listen()

        client_socket,client_address =  server_socket.accept()
        print(client_address)

        client_socket.sendall(serialized_img)
        client_socket.close()
        print('closed')
        
    except socket.timeout:
        print('time out')

server_socket.close()
