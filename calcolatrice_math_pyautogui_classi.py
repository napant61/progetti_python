"""
Nome Script: calcolatrice_math_pyautogui_classi.py
Descrizione: Questo script crea una calcolatrice che fa tre operazioni matematiche sfruttando il modulo math, ricorrendo alla libreria
pyautogui e utilizzando le classi e i metodi
Autore: Antonio Napolitano
Versione: 1.0
Data: 14/03/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""
import math
import pyautogui

class Operazione:
    def __init__(self):
        self.menu()

    def radice_quadrata(self):
        input_rq = pyautogui.prompt("Inserisci un numero positivo", "Calcolatrice avanzata")
        if input_rq:
            try:
                numero = float(input_rq)
                if numero < 0:
                    pyautogui.alert("Non puoi fare la radice quadrata di un numero negativo", "Attenzione")
                else:
                    risultato_rq = math.sqrt(numero) 
                    pyautogui.alert(f"La radice quadrata di {numero} è {risultato_rq}")
            except ValueError:
                pyautogui.alert("Inserisci un numero valido", "Attenzione")

#operazione_rq.radice_quadrata()

    def logaritmo(self):
        input_log = pyautogui.prompt("Inserisci un numero", "Logaritmo")
        if input_log:
            try:
                numero_log = float(input_log)
                if numero_log <= 0:
                    pyautogui.alert("Il numero non può essere minore di zero", "Attenzione")
                else:
                    risultato_log = math.log(numero_log)
                    pyautogui.alert(f"Il logaritmo di {numero_log} è {risultato_log}")
            except ValueError:
                pyautogui.alert("Errore, riprova", "Errore")

    def potenza(self):
        base = pyautogui.prompt("Inserisci il valore della base", "Base")
        esponente = pyautogui.prompt("Inserisci il valore dell'esponente", "Esponente")
        if base and esponente:
            try:
                base_pulita = float(base)
                esponente_pulita = float(esponente)
                risultato_pot = math.pow(base_pulita, esponente_pulita)
                pyautogui.alert(f"{base_pulita} elevato a {esponente_pulita} è uguale a {risultato_pot:.2f}")
            except ValueError:
                pyautogui.alert("Inserisci numeri validi", "Errore")

    def menu(self):
        while True:
            scelta = pyautogui.confirm("Scegli un'operazione: ", "Menu", ["Radice quadrata", "Logaritmo", "Potenza", "Esci"])
            if scelta == "Radice quadrata":
                self.radice_quadrata()
            elif scelta == "Logaritmo":
                self.logaritmo()
            elif scelta == "Potenza":
                self.potenza()
            elif scelta =="Esci":
                pyautogui.alert("Chiusura del programma", "Uscita")
                break

Operazione()            