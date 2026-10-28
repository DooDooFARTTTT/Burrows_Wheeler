import socket

server_ip = '127.0.0.1'
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

while True:
    stringa = input("inserisci la parola da bwtizzare: ")

    client.send(stringa.encode())

    if stringa.startswith("ACK:"):
        print(client.recv(1024).decode())

    recieved_string = client.recv(1024)

    print(recieved_string.decode())