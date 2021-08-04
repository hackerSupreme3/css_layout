from http.server import HTTPServer, BaseHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)

    try:
        httpd.serve_forever()
        print('Serving at ', server_address)
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print('Server stopped')


run()

