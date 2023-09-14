# webserver engines
# builtin http server (pure Python solution)

# from http.server import HTTPServer, SimpleHTTPRequestHandler

# webServer = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
# print("starting server...")
# webServer.serve_forever()


from http.server import HTTPServer, CGIHTTPRequestHandler
import cgitb
import os
import stat
cgitb.enable()
CGIHTTPRequestHandler.cgi_directories = ['/']


webServer = HTTPServer(("localhost", 8000), CGIHTTPRequestHandler)
print("starting server...")
webServer.serve_forever()
