
# date: 2019.04.14
# https://stackoverflow.com/questions/55672653/python-http-server-not-responding-on-post-and-get-requests/55672850#55672850

import http.server
import socketserver

class MyHandler(http.server.BaseHTTPRequestHandler):
    
    def do_POST(self):
        print("POST received")
		#TODO: get POST data
		
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Hello World".encode('utf-8'))


        
PORT = 8080
Handler = MyHandler #http.server.SimpleHTTPRequestHandler

with http.server.HTTPServer(("", PORT), Handler) as httpd:
#with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

