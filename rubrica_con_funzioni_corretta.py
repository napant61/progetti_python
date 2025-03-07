print("\n--------GESTIONE DI UNA RUBRICA TELEFONICA CON FUNZIONI-----------")

rubrica = {}

def aggiungi_contatto():
    nome = input("Inserisci nuovo contatto: ")
    telefono = input("Inserisci nuovo numero di telefono: ")  # Manteniamo come stringa
    indirizzo = input("Inserisci nuovo indirizzo: ")
    rubrica[nome] = {"telefono": telefono, "indirizzo": indirizzo}
    print(f"Il contatto {nome} è stato aggiunto alla rubrica.")

def visualizza_contatti():
    if rubrica:
        print("\nRUBRICA")
        for nome, dettagli in rubrica.items():
            print(f"{nome} - Telefono: {dettagli['telefono']} - Indirizzo: {dettagli['indirizzo']}")
    else:
        print("Nessun contatto in rubrica.")

def cerca_contatto():
    nome = input("Cerca contatto: ")
    if nome in rubrica:
        print(f"{nome} trovato.")
        print("\nCosa vuoi fare con questo contatto?")
        menu_cerca(nome)
    else:
        print(f"{nome} non è presente in rubrica.")

def menu_cerca(nome):
    while True:
        print("\nm. Modificarlo")
        print("e. Eliminarlo")
        print("n. Niente, torna indietro")
        scelta = input("Opzioni disponibili: ")

        if scelta == "m":
            modifica_contatto(nome)
        elif scelta == "e":
            elimina_contatto(nome)
            break  # Esce dal loop dopo l'eliminazione
        elif scelta == "n":
            break
        else:
            print("Scelta non valida, riprova.")

def modifica_contatto(nome=None):
    if nome is None:
        nome = input("Inserisci il contatto da modificare: ")
    
    if nome in rubrica:
        nuovo_telefono = input("Inserisci il nuovo numero: ")  # Manteniamo come stringa
        nuovo_indirizzo = input("Inserisci il nuovo indirizzo: ")
        rubrica[nome] = {"telefono": nuovo_telefono, "indirizzo": nuovo_indirizzo}
        print(f"Contatto {nome} aggiornato correttamente.")
    else:
        print("Il contatto che cerchi non è in rubrica.")

def elimina_contatto(nome=None):
    if nome is None:
        nome = input("Inserisci il contatto da eliminare: ")

    if nome in rubrica:
        del rubrica[nome]
        print(f"Contatto {nome} cancellato.")
    else:
        print(f"Contatto {nome} non trovato.")

def esci_programma():
    print("Uscita dal programma.")

def menu():
    while True:
        print("\nMENU OPZIONI")
        print("1. Aggiungi contatto")
        print("2. Visualizza contatti")
        print("3. Cerca contatto")
        print("4. Modifica contatto")
        print("5. Elimina contatto")
        print("6. Esci dal programma")

        scelta = input("Scegli cosa fare: ")
        if scelta == "1":
            aggiungi_contatto()
        elif scelta == "2":
            visualizza_contatti()
        elif scelta == "3":
            cerca_contatto()
        elif scelta == "4":
            modifica_contatto()
        elif scelta == "5":
            elimina_contatto()
        elif scelta == "6":
            esci_programma()
            break
        else:
            print("Scelta non valida, riprova.")

menu()
