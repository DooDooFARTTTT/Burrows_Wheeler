Server.py:
Apre la connessione a uno o più client alla prota 9999.
Riceve dal client una stringa, e se contiene un comando riconosciuto, esse verrà applciato, altrimenti inviaa al client la semplice trasformata ottenuta dallo script bwtAlgorithm importato da bwt.py

Client.py:
Stabilisce una connessione con il  server gia avviato tramite ip loopback su porta 9999.
Invia una string presa in inout dall'utente al server, questa se contiene un comando riconosciuto, l'invio o il metodo di ricezione possono essere modificati
Una volta ricevuta la trasformata, o il suo trace il client la stampa.

bwt.py:
applica l'algoritmo di Burrow-Wheeler, e qualora la flag trace sia attiva ritona anche tutti gli step effettuati

