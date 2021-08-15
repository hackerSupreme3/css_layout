import http.server
import socketserver

DIRECTORY = '../../'

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.path = '../../index.html'
            print(self.path)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler

PORT = 8000

my_server = socketserver.TCPServer(('', PORT), handler_object)

try:
    print('Server starting...')
    my_server.serve_forever()
except KeyboardInterrupt:
    pass


