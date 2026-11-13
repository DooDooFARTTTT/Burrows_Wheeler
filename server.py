import socket
from bwt import bwtAlgorithm    #importo la funzione bwtAlgorithm dal file bwt.py

port = 9999 #porta utilizzata

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #connessione tramite ipv4 tcp
server.bind(("0.0.0.0", port))  #il server si prepara ad ascoltare sulla porta tutti gli ip in arrivo
server.listen()
client, addr = server.accept()  #il server aspetta finche non arriva un client

#determina la lungezza della trasformata ottenuta da bwtAlgorithm e della traccia dei cambiamenti
#server come informazione preventiva al client prima di riceve il vero trace
def getTraceLenght(lista):          
    lenght = 0
    for i in range(len(lista)):
        lenght += len(lista[i])

    return lenght

while True:                     #la connessione dura ininterrottamente
    recieved_string = client.recv(1024)
    trace = False       #flag utilizzata per comprendere se il client ha richiesto un TRACE

    if recieved_string.startswith(b"ACK:"):     #messaggio contenente richiesta ACK
        recieved_string = recieved_string[4::]
        client.send("ciaoooo".encode())

    elif recieved_string.startswith(b"MSG:"):  #messaggio contenente richeista msg (con contenuto annesso)
        recieved_string = recieved_string[4::]
        print(recieved_string.decode())
        continue

    elif recieved_string.startswith(b"TRACE:"): #messaggio contenente richeista msg (con parola da trasformare annessa)
        recieved_string = recieved_string[6::]
        trace = True

    trasformata = bwtAlgorithm(recieved_string.decode(), trace)     #si trasforma la stringa data attravesro l'algoritmo di Burrows-Wheeler, la flag serve ad aggiugnere il tracing dell'algoritmo

    if trace:           #nel caso la flag trace sia stata attivata
        client.send(str(getTraceLenght(trasformata)).encode())  #il server invia al client la dimensione del messaggio da ricevere
        print(trasformata)          
        risposta = "\n".join(trasformata)                       #prepara la risposta aggiungendo "\n" per trasformarla in stringa
    else:
        risposta = trasformata                                  

    client.sendall(risposta.encode())
