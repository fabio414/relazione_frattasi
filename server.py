import socket

server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)