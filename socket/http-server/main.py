import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print(f'Serving HTTP on port {PORT} ...')

while True:
    print ('1 - start')
    client_connection, client_address = listen_socket.accept()
    
    # read header
    
    request_data = b''
    
    while True:
        chunk = client_connection.recv(1) # client can send header and body at once and then it is hard to find end of header b'\r\n\r\n' - other solutions save data in file buffer (ie. BytesIO) and then tehy can use readline()
        request_data += chunk
        print(chunk)
        if request_data.endswith(b'\r\n\r\n'):
            break
    
    print(request_data.decode('utf-8'))
    
    # TODO: read body if POST request and `content-length` > 0
    
    client_connection.sendall(b"""HTTP/1.1 200 OK\n\nHello, World!\n""")
    client_connection.close()
    print ('2 - end')
