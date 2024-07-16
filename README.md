# Indovina il numero
## Obiettivo: 
Due giocatori si connettono al server e cercano di indovinare un numero segreto generato dal server. Il server fornisce feedback ai giocatori dopo ogni tentativo.
## Regole:
Il server genera un numero casuale segreto (ad esempio, tra 1 e 100).
I due client si connettono al server tramite socket.
A turno, i giocatori inviano i loro tentativi al server.
Il server confronta il tentativo con il numero segreto e invia feedback:
“Il numero inserito è maggiore del ” se il tentativo è maggiore del numero segreto.
“Troppo basso” se il tentativo è minore del numero segreto.
“Hai indovinato!” se il tentativo è uguale al numero segreto.
Avrà vinto il giocatore che avrà indovinato il numero con il numero di tentativi minore.
