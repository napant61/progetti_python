"""
Nome Script: esercizio_ml3m.py
Descrizione: Analisi di Segmentazione Clienti con Clustering K-Means. Analizzare un dataset di clienti di un negozio online per identificare segmenti 
di clienti con comportamenti d'acquisto simili. Utilizzare l'algoritmo di clustering K-Means per raggruppare i clienti in base alle loro caratteristiche di spesa.
Autore: Antonio Napolitano
Versione: 1.0
Data: 19/04/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('customer_data.csv')
df['IDCliente'] = range(1, len(df) + 1)
cols = ['IDCliente'] + [col for col in df.columns if col != 'IDCliente']
df = df[cols]
print(df[['IDCliente', 'RedditoAnnuo', 'IndicediSpesa']])

# 0. Controllo dei dati
# Controllo dei dati per valori nulli e tipi di dati
print("Controllo dei dati:")
print(df.info())

# Media e deviazione standard delle colonne 'RedditoAnnuo' e 'IndicediSpesa'
print("\nStatistiche descrittive:")
print(df[['RedditoAnnuo', 'IndicediSpesa']].describe())


# 1. Normalizzazione dei dati
scaler = StandardScaler()
# L'oggetto scaler utilizza il metodo fit_transform per calcolare la media e la deviazione standard delle colonne 'RedditoAnnuo' e 'IndicediSpesa' e normalizzare i dati.
# La normalizzazione rende i dati più adatti per l'algoritmo K-Means, che è sensibile alla scala dei dati.
# Questo codice normalizza le colonne RedditoAnnuo e IndicediSpesa, portandole su una scala con media 0 e deviazione standard 1.
df[['RedditoAnnuo', 'IndicediSpesa']] = scaler.fit_transform(df[['RedditoAnnuo', 'IndicediSpesa']])

# 2. Implementazione dell'algoritno K-Means per raggruppare i clienti in un numero appropriato di cluster
# Determinazione del numero ottimale di cluster tramite il metodo del gomito (Elbow Method)

# Il metodo del gomito è una tecnica utilizzata per determinare il numero ottimale di cluster in un'analisi di clustering.
# Si basa sull'osservazione che, all'aumentare del numero di cluster, la somma delle distanze quadrate tra i punti e il centroide del cluster diminuisce.   
# Tuttavia, dopo un certo numero di cluster, l'incremento della riduzione della somma delle distanze quadrate inizia a diminuire, creando una forma simile a un gomito.
# Questo punto di "gomito" indica il numero ottimale di cluster da utilizzare.
# Per determinare il numero ottimale di cluster, si calcola la somma delle distanze quadrate tra i punti e il centroide del cluster
# per un intervallo di numeri di cluster (ad esempio, da 1 a 10).
# Si crea un grafico della somma delle distanze quadrate in funzione del numero di cluster e si cerca il punto in cui la curva inizia a "appiattirsi",
# indicando che l'aggiunta di ulteriori cluster non porta a un miglioramento significativo nella separazione dei dati.
# Questo punto è considerato il numero ottimale di cluster

# Calcolo della somma delle distanze quadrate per diversi numeri di cluster

sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df[['RedditoAnnuo', 'IndicediSpesa']])
    sse.append(kmeans.inertia_)

# Creazione del grafico del metodo del gomito
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), sse, marker='o')
plt.title('Metodo del Gomito per Determinare il Numero Ottimale di Cluster')
plt.xlabel('Numero di Cluster')
plt.ylabel('Somma delle Distanze Quadrate (SSE)')
plt.xticks(range(1, 11))
plt.grid()
plt.show()    

# 3. Creazione del modello K-Means con il numero ottimale di cluster
# In questo caso, il numero ottimale di cluster è 4, come indicato dal grafico del metodo del gomito.
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['RedditoAnnuo', 'IndicediSpesa']])

# 4. Visualizzazione dei cluster
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='RedditoAnnuo', y='IndicediSpesa', hue='Cluster', palette='viridis', s=100, alpha=0.7)
plt.title('Segmentazione Clienti con K-Means')
plt.xlabel('Reddito Annuo (Normalizzato)')
plt.ylabel('Indice di Spesa (Normalizzato)')
plt.legend(title='Cluster')
plt.grid()
plt.show()

# 5. Analisi dei cluster
# Calcolo delle statistiche per ogni cluster
cluster_stats = df.groupby('Cluster').agg({
    'RedditoAnnuo': ['mean', 'std'],
    'IndicediSpesa': ['mean', 'std'],
    'IDCliente': 'count'
}).reset_index()
cluster_stats.columns = ['Cluster', 'RedditoAnnuo_Media', 'RedditoAnnuo_DeviazioneStandard', 
                          'IndicediSpesa_Media', 'IndicediSpesa_DeviazioneStandard', 'NumeroClienti']

# Stampa delle statistiche dei cluster
print(cluster_stats)

#




