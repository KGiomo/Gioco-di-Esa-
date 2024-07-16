#!/usr/bin/env python
#
#  Server_multiplayer.py
#  
#  Giovanni Mottin
#  Data creazione: 16/12/2021
#  Ultima modifica: 20/12/2021
#
import socket, random
import threading

rangeMin = 1
rangeMax = 100

def gameServer(s1, s2, num):
	#viene inviato al client un messaggio che indica il range tra cui deve indovinare i numeri
	s1.send(f"{rangeMin},{rangeMax}".encode())
	s2.send(f"{rangeMin},{rangeMax}".encode())
	#creazione thread
	t1 = threading.Thread(target=controlliPlayers, args=(s1, num,))
	t2 = threading.Thread(target=controlliPlayers, args=(s2, num,))
	#thread start
	t1.start()
	t2.start()
	#join
	t1.join()
	t2.join()
	
	#ricevo dai client i tentativi usati per indovinare il numero
	tentativiPlayer1 = s1.recv(10).decode()
	tentativiPlayer2 = s2.recv(10).decode()
	print("")
	print("INVII CONCLUSI")
	print(f"Tentativi Player1: {tentativiPlayer1}")
	print(f"Tentativi Player2: {tentativiPlayer2}")
	
	#il server verifica il vincitore e invia ai client i risultati
	if tentativiPlayer1 == tentativiPlayer2:
		print("PAREGGIO")
		s1.send("PAREGGIO".encode())
		s2.send("PAREGGIO".encode())
	elif tentativiPlayer1 < tentativiPlayer2:
		print("HA VINTO IL GIOCATORE 1!!!")
		s1.send("HA VINTO IL GIOCATORE 1!!!".encode())
		s2.send("HA VINTO IL GIOCATORE 1!!!".encode())
	else:
		print("HA VINTO IL GIOCATORE 2!!!")
		s1.send("HA VINTO IL GIOCATORE 2!!!".encode())
		s2.send("HA VINTO IL GIOCATORE 2!!!".encode())
	
def controlliPlayers(s, num):
	while True:
		#viene letto e decodificato il messaggio ricevuto dal client
		nClient = s.recv(10).decode()
		
		print(f"Numero ricevuto: {nClient}")
		
		#viene inviato al client un feedback sul numero ricevuto
		if int(num) == int(nClient):
			s.send("=".encode())
			break
		elif int(nClient) > num:
			s.send(">".encode())
		else:
			s.send("<".encode())
	
def main(args):
	
	#creo il primo socket
	connection1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#imposta il socket in modo che liberi la porta quando si disconnette, anche senza l'uso del metodo close()
	connection1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#definisco la tupla composta dall'indirizzo e dalla porta a cui il client si connetterà
	server = ("localhost", 1234)
	#associo il socket creato alla tupla con l'indirizzo e la porta
	connection1.bind(server)
	#abilito l'ascolto da parte del socket
	connection1.listen()
	#faccio rimanere il socket in ascolto, restituendo il socket e l'indirizzo del client
	sock1, client_addr1 = connection1.accept()
	
	#creo il secondo socket
	connection2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#imposta il socket in modo che liberi la porta quando si disconnette, anche senza l'uso del metodo close()
	connection2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#associo il socket creato alla tupla con l'indirizzo e la porta
	#definisco la tupla composta dall'indirizzo e dalla porta a cui il client si connetterà
	server = ("localhost", 1235)
	connection2.bind(server)
	#abilito l'ascolto da parte del socket
	connection2.listen()
	#faccio rimanere il socket in ascolto, restituendo il socket e l'indirizzo del client
	sock2, client_addr2 = connection2.accept()
	
	#ora che sono stabilite le connessioni è possibile avviare il gioco
	sock1.send("START".encode())
	sock2.send("START".encode())
	
	#viene creato un numero random da rangeMin a rangeMax
	nServer = random.randint(rangeMin, rangeMax)
	print(f"Numero generato: {nServer}")
	
	#comincio la partita
	gameServer(sock1, sock2, nServer)
	
	#chiudo la connessione stabilita dal socket
	connection1.close()
	connection2.close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
