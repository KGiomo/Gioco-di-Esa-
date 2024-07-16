#!/usr/bin/env python
#
#  Client_multiplayer.py
#  
#  Giovanni Mottin
#  Data creazione: 16/12/2021
#  Ultima modifica: 20/12/2021
#
import socket, re

def gameClient(s):
	count = 0
	
	numRange = s.recv(10).decode()
	rangeMin = int(numRange.split(",", 1) [0])
	rangeMax = int(numRange.split(",", 1) [1])
	
	print("Lo scopo del gioco è indovinare il numero scelto dal server nel minor numero di tentativi\n")
	print("Ogni carettere o numero inserito verrà conteggiato come tentativo\n")
	
	while True:
		count += 1
		MyN = input("Inserisci un numero: ")
		
		#faccio inviare al server il numero inserito, dopo averlo trasformato in una stringa e codificato in byte
		s.send(str(MyN).encode())
		
		#ricevo e decodifico il messaggio del server
		ris = s.recv(1).decode()
		
		#in base al messaggio ricevuto dal server viene fornito un feedback sul numero inserito
		if ris == "=":
			print(f"Complimenti hai indovinato il numero!!!.... Tentativi impiegati: {count}\n")
			#invio al server i tentativi impiegati dal client
			s.send(str(count).encode())
			#lettura del vincitore
			print(s.recv(30).decode())
			break
		elif ris == ">":
			print(f"Il numero inserito è maggiore del numero da indovinare")
		else:
			print(f"Il numero inserito è minore del numero da indovinare")
	
def main(args):
	#creo il socket
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#definisco la tupla composta dall'indirizzo e dalla porta a cui il client si connetterà
	server = ("localhost", 1235)
	#associo il socket creato alla tupla con l'indirizzo e la porta
	connection.connect(server)
	
	#START
	print(connection.recv(5).decode())
	
	#comincio la partita
	gameClient(connection)
	
	#chiudo la connessione stabilita dal socket
	connection.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
