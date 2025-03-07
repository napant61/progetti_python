class Contatto:
    """Classe che rappresenta un contatto."""
    def __init__(self, nome, telefono, indirizzo):
        self.nome = nome
        self.telefono = telefono
        self.indirizzo = indirizzo

    def __str__(self):
        """Rappresentazione testuale di un contatto."""
        return f"{self.nome} - Telefono: {self.telefono} - Indirizzo: {self.indirizzo}"


class Rubrica:
    """Classe che gestisce una rubrica telefonica."""
    def __init__(self):
        self.contatti = {}

    def aggiungi_contatto(self):
        nome = input("Inserisci nuovo contatto: ")
        telefono = input("Inserisci nuovo numero di telefono: ")
        indirizzo = input("Inserisci nuovo indirizzo: ")

        if nome in self.contatti:
            print("Il contatto esiste già.")
        else:
            self.contatti[nome] = Contatto(nome, telefono, indirizzo)
            print(f"Il contatto {nome} è stato aggiunto alla rubrica.")

    def visualizza_contatti(self):
        if self.contatti:
            print("\nRUBRICA")
            for contatto in self.contatti.values():
                print(contatto)
        else:
            print("Nessun contatto in rubrica.")

    def cerca_contatto(self):
        nome = input("Cerca contatto: ")
        if nome in self.contatti:
            print("\nContatto trovato:")
            print(self.contatti[nome])
            self.menu_cerca(nome)
        else:
            print(f"{nome} non è presente in rubrica.")

    def menu_cerca(self, nome):
        while True:
            print("\nCosa fuoi farne?")
            print("\nm. Modificarlo")
            print("e. Eliminarlo")
            print("n. Niente, torna indietro")
            scelta = input("Opzioni disponibili: ")

            if scelta == "m":
                self.modifica_contatto(nome)
            elif scelta == "e":
                self.elimina_contatto(nome)
                break  # Esce dal loop dopo l'eliminazione
            elif scelta == "n":
                break
            else:
                print("Scelta non valida, riprova.")

    def modifica_contatto(self, nome=None):
        if nome is None:
            nome = input("Inserisci il contatto da modificare: ")

        if nome in self.contatti:
            nuovo_telefono = input("Inserisci il nuovo numero: ")
            nuovo_indirizzo = input("Inserisci il nuovo indirizzo: ")
            self.contatti[nome] = Contatto(nome, nuovo_telefono, nuovo_indirizzo)
            print(f"Contatto {nome} aggiornato correttamente.")
        else:
            print("Il contatto che cerchi non è in rubrica.")

    def elimina_contatto(self, nome=None):
        if nome is None:
            nome = input("Inserisci il contatto da eliminare: ")

        if nome in self.contatti:
            del self.contatti[nome]
            print(f"Contatto {nome} cancellato.")
        else:
            print(f"Contatto {nome} non trovato.")

    def esci_programma(self):
        print("Uscita dal programma.")


def menu():
    rubrica = Rubrica()

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
            rubrica.aggiungi_contatto()
        elif scelta == "2":
            rubrica.visualizza_contatti()
        elif scelta == "3":
            rubrica.cerca_contatto()
        elif scelta == "4":
            rubrica.modifica_contatto()
        elif scelta == "5":
            rubrica.elimina_contatto()
        elif scelta == "6":
            rubrica.esci_programma()
            break
        else:
            print("Scelta non valida, riprova.")


menu()