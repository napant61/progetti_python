"""
Nome Script: calcolatrice_math_tkinter.py
Descrizione: Questo script crea una calcolatrice che fa tre operazioni matematiche sfruttando il modulo math, ricorrendo alla libreria
tkinter
Autore: Antonio Napolitano
Versione: 1.0
Data: 14/03/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""

from tkinter import Tk, Label, Entry, Button, StringVar
import math

# definizione delle variabili che faranno i calcoli
def calcola(inserimento_numero, risultato, operazione):
    try:
        numero = float(inserimento_numero.get())
        if operazione == "radice_quadrata":
            risultato1.set(math.sqrt(numero))
        elif operazione == "logaritmo":
            if numero <= 0:
                risultato2.set("Errore: il numero non può essere minore o uguale a 0")
            else:
                risultato2.set(math.log(numero))
        else:
            risultato1.set("Errore: operazione non valida")
    except ValueError:
        risultato1.set("Errore: inserire almeno un numero")

# creazione della finestra principale
finestra = Tk()
finestra.title("Calcolatrice con math e tkinter")

# creazione delle variabili per i due calcoli
inserimento_numero = StringVar()
risultato1 = StringVar()
risultato2 = StringVar()

# creazione funzione di reset
def reset():
    inserimento_numero.set("")
    risultato1.set("")
    risultato2.set("")

# Riga per inserimento numero
Label(finestra, text="Inserisci un numero:").grid(row=0, column=0, padx=10, pady=10)
Entry(finestra, textvariable=inserimento_numero).grid(row=0, column=1, padx=10, pady=10)

# Prima riga: calcolo della radice quadrata
Label(finestra, text= "Radice quadrata:").grid(row=1, column=0, padx=10, pady=10)
Button(finestra, text="Calcola", command= lambda: calcola(inserimento_numero, risultato1, "radice_quadrata")).grid(row=1, column=2, padx=10, pady=10)
Entry(finestra, textvariable=risultato1).grid(row=1, column=3, padx=10, pady=10)

# Seconda riga: calcolo del Logaritmo naturale
Label(finestra, text="Logaritmo naturale:").grid(row=2, column=0, padx=10, pady=10)
Button(finestra, text="Calcola", command= lambda: calcola(inserimento_numero, risultato2, "logaritmo")).grid(row=2, column=2, padx=10, pady=10)
Entry(finestra, textvariable=risultato2).grid(row=2, column=3, padx=10, pady=10)

# Terza riga: pulsante di reset
Button(finestra, text="Annulla", command= reset).grid(row=3, column=3, padx=10, pady=10)

finestra.mainloop()


                           