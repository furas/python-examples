#import socketserver
import http.server

class MyTCPHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print('GET', self.headers)
        #print(dir(self))
        print(self.address_string)
        print(self.client_address)
        print(self.command)
        print(self.connection)
        print(self.date_time_string)
        print(self.default_request_version)
        print(self.error_content_type)
        print(self.error_message_format)
        print(self.log_date_time_string)
        print(self.log_error)
        print(self.log_message)
        print(self.log_request)
        print(self.monthname)
        print(self.path)
        print(self.protocol_version)
        print(self.raw_requestline)
        
        # send raw data
        self.request.sendall(b'HTTP/1.0 200 OK\nContent-type: text/html\n\n<h1>Hello Raw World!</h1>')

        # send the same
#        self.send_response(200)
#        self.send_header("Content-type", "text/html")
#        self.end_headers()
#        self.wfile.write('<h1>Hello World!</h1>'.encode())

        
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    try:
        server = http.server.HTTPServer((HOST, PORT), MyTCPHandler)
        print('Running http://{}:{}'.format(HOST, PORT))
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
    finally:
        # close server so port will be free in next start
        server.server_close()
