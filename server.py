import socket

server = socket.socket()
server.bind(("localhost", 12345))
server.listen(1)

print("Server avviato")

conn, addr = server.accept()

testo = conn.recv(1024).decode()

s = testo + "$"

rotazioni = []


for i in range(len(s)):
    rotazioni.append(s[i:] + s[:i])

rotazioni.sort()

bwt = ""