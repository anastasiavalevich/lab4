from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        status = 200  # меняется в дальнейшем
        if self.path == '/':
            response_body = bytes("<h1>Does it work?</h1>", encoding='utf-8')
        else:
            response_body = bytes("<h1>404 Not Found</h1>", encoding='utf-8')
            status = 404

        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(response_body)


def runserver(server_class=HTTPServer, handler_class=HttpProcessor):
    server_address = ('0.0.0.0', 80)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()


if __name__ == '__main__':
    runserver()
