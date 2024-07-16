# Indovina il numero
## Obiettivo: 
Due giocatori si connettono al server e cercano di indovinare un numero segreto generato dal server. Il server fornisce feedback ai giocatori dopo ogni tentativo.
## Regole:
Il server genera un numero casuale segreto tra 1 e 100 (è possibile personalizzare anche il range eseguendo una modifica alle variabili del range).  
I due client si connettono al server tramite socket ed a turno inviano i loro tentativi al server.  
Il server confronta il tentativo con il numero segreto e invia un feedback:  
“>” se il tentativo è maggiore del numero segreto.  
“<” se il tentativo è minore del numero segreto.  
“=” se il tentativo è uguale al numero segreto (ovviamente viene interrotto l'inserimento dei valori).  
Il server controlla il numero dei tentativi effettuati da ogni giocatore e comunicherà chi avrà indovinato il numero con il numero di tentativi minore.  
