from http.server import HTTPServer, BaseHTTPRequestHandler

server_address = ('', 8000)

sample_page = open(b"../../index.html")
page_html = sample_page.read()
sample_page.close()

sample_css = open(b'../../styles/main.css')
page_css = sample_css.read()
sample_css.close()
 
class NewServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        test_url = self.path
        self.wfile.write(bytes(test_url, "utf-8"))

        if self.path == '/':
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(page_html, "utf-8"))

        #if self.path == '/styles/main.css':
         #   self.send_header('Content-type', 'text/css')
          #  self.end_headers()
           # self.wfile.write(bytes(page_css, "utf-8"))

if __name__ == "__main__":
    myServer = HTTPServer(server_address, NewServer)
    print("Serving started http://%s", server_address)

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




