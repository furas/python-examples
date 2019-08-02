import socket
import cv2 
import pickle

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4000))

cv2.namedWindow('client')

while True:
    serialized_image = b""

    serialized_len = client_socket.recv(8) # always length 8
    length = pickle.loads(serialized_len) 
    #print('length:', length)

    while length > 0:
        if length < 1024:
            packet = client_socket.recv(length)
        else:
            packet = client_socket.recv(1024)
            
        if not packet:
            print('error: no data')
            break
        
        serialized_image += packet
        length -= len(packet)
    
    #print('received:', len(serialized_image))
    
    image = pickle.loads(serialized_image)
    cv2.imshow('client', image)
    
    # it need it to display image (maybe it has to receive events from system)
    # it `waitKey` waits 10ms so it doesn't block loop
    key = cv2.waitKey(10) & 0XFF
    if key == 27:
        break
        
cv2.destroyAllWindows()

