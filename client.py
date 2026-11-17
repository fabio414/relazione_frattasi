import socket

client = socket.socket()
client.connect(("localhost", 12345))

testo = input("Inserisci stringa: ")

client.send(testo.encode())

risposta = client.recv(1024).decode()

print("BWT:", risposta)

client.close()