"""
Nome Script: calcolatrice_math.py
Descrizione: Questo script crea una calcolatrice che sfrutta il modulo math per fare 3 operazioni matematiche
Autore: Antonio Napolitano
Versione: 1.0
Data: 14/03/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""
import math

class Operazione:
    def __init__ (self, nome):
        self.nome = nome
    
    def radice_quadrata(self):
        rq = float(input("Inserisci un numero: "))
        if rq < 0:
            print("Errore: non si può calcolare la radice quadrata di un numero negativo")
            return
        valore_rq = math.sqrt(rq)
        print(f"La radice quadrata di {rq}  è {valore_rq}")
    
    def logaritmo(self):
        log = float(input("Inserisci un numero: "))
        if log <= 0:
            print("Errore: si può calcolare il logaritmo solo per numeri positivi")
            return
        valore_log = math.log(log)
        print(f"Il logaritmo naturale di {log} è {valore_log}")

    def potenza(self):
        base = float(input("Inserisci il valore della base: "))
        esponente = float(input("Inserisci il valore dell'esponente: "))
        valore_potenza = math.pow(base, esponente)
        print(f"{base} elevato a {esponente} è pari a: {valore_potenza}")
        

class Menu:
    def __init__(self):
        self.operazione = Operazione("Calcoli matematici con math")
    def mostra_menu(self):    
        while True:
            print("\nOpzioni di calcolo")
            print("1. Radice quadrata")
            print("2. Logaritmo in base naturale")
            print("3. Elevazione a potenza")
            print("4. Esci dal programma")

            scelta_opzione = input("\nScegli cosa fare:")
            if scelta_opzione == "1":
                self.operazione.radice_quadrata()
            elif scelta_opzione == "2":
                self.operazione.logaritmo()
            elif scelta_opzione == "3":
                self.operazione.potenza()
            elif scelta_opzione == "4":
                print("Esci dall'operazione")
                break
            else:
                print("Insersci valori validi")

menu = Menu()
menu.mostra_menu()