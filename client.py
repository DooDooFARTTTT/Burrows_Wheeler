import socket
server_ip = '127.0.0.1' #il client comunica con l'ip loopback al processo server sul pc
port = 9999 #porta utilizzata

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #connessione tramite ipv4 tcp
client.connect((server_ip, port)) #il client si connette al server

while True:                 #ciclo infinito di lavoro del client
    stringa = input("inserisci la parola da bwtizzare: ")   #presa in input del comando e o parola da trasformare
    recieved_string = ""                    #stringa ricevuta dal client dal server, utilizzata in caso di trace per contenere i vari chunk inviati

    client.send(stringa.encode())           #invio del comando e o parola da trasforamre

    if stringa.startswith("ACK:"):          #ACK, richeide al server una risposta, non passa attraverso la normale ricezione client
        print(client.recv(1024).decode())
        continue
    if stringa.startswith("MSG:"):          #MSG, tutto il testo dopo : verra preso come messaggio e inviato al server, non passa attraverso la normale ricezione client
        continue
    if stringa.startswith("TRACE:"):        #TRACE, richiede al server di inviare anche i vari steps eseguit dallo script bwt, non passa attraverso la normale ricezione client
        lenght = float(client.recv(16).decode())        #lunghezza del messaggio in arrivo, necessaria per determinare quanti dati vanno richiesti
        print("LUNGHEZZA: " + str(lenght) + "\n")
        recieved_bytes = 0                      #numero di bytes ricevuti totali dal client durante il trace
        while recieved_bytes < lenght:          #finche i bytes ricevuti non sono uguali a quelli da ricevere
            chunk = client.recv(1024)           #il chunk è un buffer momentaneo che contiene tutti i dari ricevuti durante un singolo recv
            recieved_string = recieved_string + chunk.decode()      #la stringa totale si aggiorna con il contenuto del chink
            recieved_bytes = len(recieved_string)                   #il totale di bytes ricevuti è uguale alla lugnezza dei bytes ricevuti
        #fine loop di ricezione
            
        print(recieved_string, flush=True)                  #forza lo svuotamento immediato del buffer output del print, in modo da stampare facilmente contenuti lunghi
        chunk = ""                  #reset del chunk
        lenght = 0                  #reset lunghezza prestabilità
        recieved_bytes = 0          #reset buffer di dati ricevuti
        continue
             
        

    recieved_string = client.recv(1024)  #riceve dal server la strigna di dati traformata
    print(recieved_string.decode())      #stampa il contenuto della stringa ricevuta dal server