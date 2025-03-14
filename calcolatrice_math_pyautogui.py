"""
Nome Script: calcolatrice_math_pyautogui.py
Descrizione: Questo script crea una calcolatrice che fa tre operazioni matematiche sfruttando il modulo math e ricorrendo alla libreria pyautogui
Autore: Antonio Napolitano
Versione: 1.0
Data: 14/03/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""
import math
import pyautogui

pyautogui.alert("Calcola la radice quadrata", "Calcolatrice avanzata")
input_rq = pyautogui.prompt("Inserisci un numero", "Radice quadrata")
if input_rq:
    try:
        numero = float(input_rq)
        if numero < 0:
            pyautogui.alert("Attenzione, non puoi fare la radice quadrata di un numero negativo", "Attenzione!")
        else:
            risultato = math.sqrt(numero)
            pyautogui.alert(f"La radice quadrata di {numero} è {risultato}")
    except ValueError:
        pyautogui.alert("Inserisci un numero valido", "Errore!")        

else:
    pyautogui.alert("Ripeti l'operazione", "Attenzione!")

pyautogui.alert("Calcola il logaritmo", "Calcolatrice avanzata")
input_log = pyautogui.prompt("Inserisci un numero", "Logaritmo")
if input_log:
    try:
        numero_log = float(input_log)
        if numero_log <= 0:
            pyautogui.alert("Errore: non si può calcolare il logaritmo di un numero negativo")
        else:
            risultato_log = math.log(numero_log)
            pyautogui.alert(f"Il logaritmo di {numero_log} è {risultato_log}")
    except ValueError:
        pyautogui.alert("Inserisci un numero valido", "Errore!")
else:
    pyautogui.alert("Ripeti l'operazione", "Attenzione!")   

pyautogui.alert("Calcola l'elevazione a potenza", "Calcolatrice avanzata")
input_base = pyautogui.prompt("Inserisci la base", "Base")
input_esponente = pyautogui.prompt("Inserisci l'esponente", "Esponente")
if input_base is not None and input_esponente is not None:
    try:
        base = float(input_base)
        esponente = float(input_esponente)
        risultato_pot = math.pow(base, esponente)
        pyautogui.alert(f"{base} elevato a {esponente} è: {risultato_pot}")
    except ValueError:
        pyautogui.alert("Errore: inserisci numeri validi", "Errore!")
else:
    pyautogui.alert("Operazione annullata", "Fine")