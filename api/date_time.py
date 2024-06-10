# This module defines classes for implementing HTTP servers.
# This class is used to handle the HTTP requests that arrive at the server. 

# for datetime library you can use much more from here : https://www.programiz.com/python-programming/datetime


from http.server import BaseHTTPRequestHandler
# from datetime import datetime
from datetime import date 

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # the status
        self.send_response(200)
        # the type of the function output
        self.send_header('Content-type','text/plain')
        self.end_headers()
        # will put the results inside file called wfile 
        today = date.today() 
        # self.wfile.write(str(today.day).encode())
        self.wfile.write(str(today.month).encode())
        # self.wfile.write(str(today.year).encode())
        # self.wfile.write(str(datetime.now().strftime('%H:%M:%S')).encode())
        return