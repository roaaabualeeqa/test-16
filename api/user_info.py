from http.server import BaseHTTPRequestHandler
from urllib import parse 
class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        s = self.path
        print("path....",s)
        # /api/user_info?name=mais&age=25
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        print( query_string_list)
        my_dictionary = dict(query_string_list)

        # if the key doesn't exist will return False and render what is inside else  

        name = my_dictionary.get('name', False)
        age = my_dictionary.get('age', False)
        if name :
            msg = f'hello {name} and your age is {age}' 
        else:
           msg="heey! but who you are!!"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(msg.encode())
        return