import socket
server_ip = '127.0.0.1'
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

while True:
    stringa = input("inserisci la parola da bwtizzare: ")
    recieved_string = ""

    client.send(stringa.encode())

    if stringa.startswith("ACK:"):
        print(client.recv(1024).decode())
    if stringa.startswith("MSG:"):
        continue
    if stringa.startswith("TRACE:"):
        lenght = float(client.recv(16).decode())
        print("LUNGHEZZA: " + str(lenght) + "\n")
        recieved_bytes = 0
        while recieved_bytes < lenght:
            chunk = client.recv(1024)
            recieved_string = recieved_string + chunk.decode()
            recieved_bytes = len(recieved_string)
            
        print(recieved_string, flush=True)
        chunk = ""
        lenght = 0
        recieved_bytes = 0
        continue
             
        

    recieved_string = client.recv(1024)
    print(recieved_string.decode())