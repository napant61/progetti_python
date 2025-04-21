"""
Nome Script: esercizio_mlm4.py
Descrizione: Creazione del dataset per l'esercizio di clustering KMeans. Ho generato dei dati casuali realistici per riprodurre correttamente il dataset.
Inoltre ho creato un file csv con i dati generati.
Autore: Antonio Napolitano
Versione: 1.0
Data: 19/04/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""

import pandas as pd
import numpy as np

# procediamo alla creazione del dataset necessario
# generiamo dati casuali realistici per riprodurre correttamente il dataset
np.random.seed(42)

# stabiliamo un mumero credibile di clienti
numero_clienti = 300

# creiamo i due set di dati randomici relativi a reddito annuo e all'indice di spesa
reddito_annuo = np.random.randint(15, 150, numero_clienti) * 1000 # spiegazione: il reddito in formato numero intero da 15 mila a 150 mila
indice_spesa = np.random.randint(1, 101, numero_clienti) # spiegazione: il punteggio di spesa tra 1 e 100

# creiamo un dizionario con i dati sopra
data = {
    'RedditoAnnuo': reddito_annuo,
    'IndicediSpesa': indice_spesa
}

# creiamo il dataframe
df = pd.DataFrame(data)

# creazione del file csv da utilizzare per l'esercizio
nome_file = 'customer_data.csv'

# esportiamo il dataframe nel file csv appena creato
df.to_csv(nome_file, index= False)
print(f"I dati sono stati salvati nel file '{nome_file}")

