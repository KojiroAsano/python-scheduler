
from http.server import ThreadingHTTPServer, CGIHTTPRequestHandler

serverAddress = 'localhost'
serverPort = 80
server = ThreadingHTTPServer(
    (serverAddress, serverPort), CGIHTTPRequestHandler)

print('serving at' + str(serverAddress) + ' : ' + str(serverPort))
server.serve_forever()