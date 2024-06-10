from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list=parse.parse_qsl(url_components.query)
        my_dictionary=dict(query_string_list)
        arrayof_definitions=[]
        if 'word' in my_dictionary:

            # send a request to thired part API

            # /api/api_request?word=mobile
            word = my_dictionary['word']
            url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
            # add the word to the end of url
            req =requests.get(url+word)
            # save the data in JSON format
            received_data =req.json()
            for word_data in received_data :
                # to reach the first object in definitions 
                definitions_result = word_data['meanings'][0]['definitions'][0]['definition']
                arrayof_definitions.append(definitions_result)
            msg = str(arrayof_definitions)    
        else:
            msg = "please enter a word!!" 

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(msg.encode())
        return