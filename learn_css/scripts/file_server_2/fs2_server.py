from http.server import HTTPServer, BaseHTTPRequestHandler

server_address = ('', 8000)

class NewServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>joysdickisbig</title></head><body><p>suckmyballs</p></body></html>", "utf-8"))

if __name__ == "__main__":
    myServer = HTTPServer(server_address, NewServer)
    print("Serving started http://%s:%s", server_address[0], server_address[1])

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass
    
    print('Server jizzed out')

#def run(server_class=HTTPServer, handler_class=BaseHTTPRequeerve_forever)
    #server_address = ('', 8000)
    #httpd = server_class(server_address, handler_class)

    #try:
    #    httpd.serve_forever()
    #    print('Serving at ', server_address)
    #except KeyboardInterrupt:
    #    pass

    #httpd.server_close()
    #print('Server stopped')




