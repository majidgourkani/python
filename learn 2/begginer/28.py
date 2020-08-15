import http.server
import socketserver

PORT = 4444

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("" , PORT) , handler) as httpd:
    print("Server Work on Port 4444")
    httpd.serve_forever()

#server root is evry-where script is
