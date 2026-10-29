import socket
import time

server_ip = '127.0.0.1'
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

while True:
    stringa = input("inserisci la parola da bwtizzare: ")
    recieved_string = ""

    if stringa.startswith("PING:"):
            stringa = stringa + str(time.perf_counter())
            client.send(stringa.encode())
            print(float(client.recv(1024).decode()) * 1000)

    client.send(stringa.encode())

    if stringa.startswith("ACK:"):
        print(client.recv(1024).decode())
    if stringa.startswith("MSG:"):
        continue
    if stringa.startswith("TRACE:"):
        lenght = float(client.recv(4).decode())
        recieved_bytes = 0
        while recieved_bytes < lenght:
            chunk = client.recv(512)
            recieved_string = recieved_string + chunk.decode()
            recieved_bytes = len(recieved_string)
        print(recieved_string)
        continue
             
        

    recieved_string = client.recv(1024)
    print(recieved_string.decode())