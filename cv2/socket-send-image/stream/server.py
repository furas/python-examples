import socket
import cv2
import pickle

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 4000))

cap = cv2.VideoCapture(0)
    
while True:
    try:
        server_socket.listen()

        print('waiting ...')
        client_socket,client_address =  server_socket.accept()
        print(client_address)

        while True:
            try:
                ret, img = cap.read()
        
                serialized_img = pickle.dumps(img)
                print('serialized_len:', len(serialized_img))
        
                serialized_len = pickle.dumps(len(serialized_img))
                #print('len(serialized_len):', len(serialized_len)) # always length 8
        
                client_socket.sendall(serialized_len) # always length 8
                client_socket.sendall(serialized_img)
            except Exception as ex:
                print(ex)
                # exit loop when errro, ie. when client close connection
                break 
                
        client_socket.close()
        print('closed')
        
    except socket.timeout:
        print('time out')

cap.release()
server_socket.close()
