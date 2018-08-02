from http.server import HTTPServer, CGIHTTPRequestHandler


port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port:{0}".format(str(httpd.server_port)))
httpd.serve_forever()