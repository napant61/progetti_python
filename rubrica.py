print("\n--------GESTIONE DI UNA RUBRICA TELEFONICA SENZA FUNZIONI-----------")

rubrica = {}

while True:
    print("\nMENU GENERALE")
    print("1. Aggiungi contatto")
    print("2. Visualizza contatti")
    print("3. Cerca un contatto")
    print("4. Modifica un contatto")
    print("5. Elimina un contatto")
    print("6. Uscita dal programma")
    
    scelta_utente = input("Scegli un'opzione da 1 a 6: ")

    if scelta_utente == "1":
        nome = input("Inserisci un nome: ")
        telefono = input("Inserisci il numero di telefono: ")
        indirizzo = input("Inserisci l'indirizzo: ")
        rubrica[nome] = {"telefono": telefono, "indirizzo": indirizzo}
        print(f"Il contatto {nome} è stato aggiunto alla rubrica")

    elif scelta_utente == "2":
        if rubrica:
            print("\n--Rubrica--")
            for nome, dati in rubrica.items():
                print(f"{nome}: Telefono: {dati['telefono']}, Indirizzo: {dati['indirizzo']}")
        else:
            print("La rubrica è vuota!")

    elif scelta_utente == "3":
        nome = input("Inserisci il nome da cercare: ")
        if nome in rubrica:
            print(f"{nome}: Telefono: {rubrica[nome]['telefono']}, Indirizzo: {rubrica[nome]['indirizzo']}")
        else:
            print("Il nome cercato non esiste")

    elif scelta_utente == "4":
        nome = input("Inserisci il nome del contatto da modificare: ")
        if nome in rubrica:
            nuovo_numero = input(f"Inserisci il nuovo numero per il contatto {nome}: ")
            nuovo_indirizzo = input(f"Inserisci il nuovo indirizzo per il contatto {nome}: ")
            rubrica[nome] = {"telefono": nuovo_numero, "indirizzo": nuovo_indirizzo}
            print("Contatto aggiornato correttamente")
        else:
            print("Contatto non trovato")

    elif scelta_utente == "5":
        nome = input("Inserisci il nome del contatto da cancellare: ")
        if nome in rubrica:
            del rubrica[nome]
            print(f"Contatto {nome} cancellato!")
        else:
            print(f"Contatto {nome} non trovato")

    elif scelta_utente == "6":
        print("Uscita dal programma")
        break
    
    else:
        print("Scelta non valida, riprova.")