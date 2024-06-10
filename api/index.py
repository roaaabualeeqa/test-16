from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

          # the status
        self.send_response(200)
        # the type of the function output
        self.send_header('Content-type','text/plain')
        self.end_headers()
        msg="welcome from 401 python class"
        self.wfile.write(msg.encode())
        return