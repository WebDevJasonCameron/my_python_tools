# server.py
import http.server
import socketserver

PORT = 8000
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Serving on port", PORT)
    httpd.serve_forever()
