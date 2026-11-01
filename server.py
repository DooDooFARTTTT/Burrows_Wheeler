import socket
from bwt import bwtAlgorithm

port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", port))
server.listen()
client, addr = server.accept()

def getTraceLenght(lista):
    lenght = 0
    for i in range(len(lista)):
        lenght += len(lista[i])

    return lenght

while True:
    recieved_string = client.recv(1024)
    trace = False

    if recieved_string.startswith(b"ACK:"):
        recieved_string = recieved_string[4::]
        client.send("ciaoooo".encode())
    elif recieved_string.startswith(b"MSG:"):
        recieved_string = recieved_string[4::]
        print(recieved_string.decode())
        continue
    elif recieved_string.startswith(b"TRACE:"):
        recieved_string = recieved_string[6::]
        trace = True

    trasformata = bwtAlgorithm(recieved_string.decode(), trace)

    if trace:
        client.send(str(getTraceLenght(trasformata)).encode())
        print(trasformata)
        risposta = "\n".join(trasformata)
    else:
        risposta = trasformata

    client.sendall(risposta.encode())
