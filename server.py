import socket
from bwt import bwtAlgorithm

port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", port))
server.listen()
client, addr = server.accept()


while True:
    recieved_string = client.recv(1024)

    if recieved_string.startswith(b"ACK:"):
        recieved_string = recieved_string[4::]
        client.send("ciaoooo".encode())
    elif recieved_string.startswith(b"MSG:"):
        recieved_string = recieved_string[4::]
        print(recieved_string.decode())
        continue

    client.send(bwtAlgorithm(recieved_string.decode()).encode())
