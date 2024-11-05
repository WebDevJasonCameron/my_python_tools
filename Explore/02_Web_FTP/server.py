#!/usr/bin/env python3
# server.py
import http.server

PORT = 8000
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

with http.server.HTTPServer(("", PORT), handler) as httpd:
    print("Serving on port", PORT)
    httpd.serve_forever()