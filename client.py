import socket
import time

server_ip = '127.0.0.1'
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

while True:
    stringa = input("inserisci la parola da bwtizzare: ")

    client.send(stringa.encode())

    if stringa.startswith("ACK:"):
        print(client.recv(1024).decode())
    if stringa.startswith("MSG:"):
        continue
    if stringa.startswith("PING"):
        client.send(str(time.perf_counter()).encode())
        print(float(client.recv(1024).decode()) * 1000)
        continue
        

    recieved_string = client.recv(1024)

    print(recieved_string.decode())