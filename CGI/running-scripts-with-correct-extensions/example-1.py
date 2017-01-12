#!/usr/bin/env python3

import BaseHTTPServer
import CGIHTTPServer

class MyHandler(CGIHTTPServer.CGIHTTPRequestHandler):

    cgi_exts = ['.py']

    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            try:
                self.wfile.write("ABBA\n")
            finally:
                f.close()

    def is_cgi(self):
        collapsed_path = _url_collapse_path(self.path)
        dir_sep = collapsed_path.find('/', 1)
        head, tail = collapsed_path[:dir_sep], collapsed_path[dir_sep+1:]
        if head in self.cgi_directories:
            if tail.endswith('.py'):
                self.cgi_info = head, tail
                return True
        return False

server = BaseHTTPServer.HTTPServer(('', 8000), MyHandler)
server.serve_forever()

