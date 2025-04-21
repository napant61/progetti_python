"""
Nome Script: esercizio_ml3m_alternativa.py
Descrizione: Questa analisi utilizza l'algoritmo K-Means per segmentare i clienti di un negozio online in base al loro reddito annuale
e al punteggio di spesa. L'obiettivo è identificare gruppi omogenei di clienti con comportamenti di spesa simili per strategie di marketing mirate.
Ho utilizzato i suggerimenti di DEEPSEEK in alternativa a quelli di COPILOT per vedere le differenze di procedura e di codice.
Autore: Antonio Napolitano
Versione: 1.0
Data: 21/04/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. CARICAMENTO ED ESPLORAZIONE DEI DATI  
# Caricamento dei dati
df = pd.read_csv('customer_data.csv')

# Aggiungere la colonna 'IDCliente' come prima colonna al dataset
df['IDCliente'] = range(1, len(df) + 1)
cols = ['IDCliente'] + [col for col in df.columns if col != 'IDCliente']
df = df[cols]

# Visualizzazione delle prime righe
print(df.head())

# Statistiche descrittive
print(df.describe())

# Plot iniziale
plt.scatter(df['RedditoAnnuo'], df['IndicediSpesa'])
plt.xlabel('Reddito Annuale')
plt.ylabel('Punteggio di Spesa')
plt.title('Distribuzione Clienti')
plt.show()

# 2. PREPROCESSING
# Selezione delle feature rilevanti
X = df[['RedditoAnnuo', 'IndicediSpesa']]

# Standardizzazione dei dati
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. DETERMINAZIONE DEL NUMERO OTTIMALE DI CLUSTER (METODO DEL GOMITO)
somma_quadrati = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    somma_quadrati.append(kmeans.inertia_)

# grafico del metodo del gomito
plt.plot(range(1,11), somma_quadrati)
plt.title('Metodo del gomito')
plt.xlabel('Numero di cluster')
plt.ylabel('Somme dei quadrati dei cluster')
plt.grid()
plt.show()

# 4. APPLICAZIONE DEL K-MEANS
# Scegliamo 5 cluster basandoci sul metodo del gomito.
# DeepSeek suggerisce 5 cluster mentre Copilot ne individuava solo 4.
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Aggiunta dei cluster al dataframe originale
df['Cluster'] = clusters

# 5. VISUALIZZAZIONE DEI RISULTATI
plt.scatter(X_scaled[clusters == 0, 0], X_scaled[clusters == 0, 1], s=50, c='red', label='Cluster 1')
plt.scatter(X_scaled[clusters == 1, 0], X_scaled[clusters == 1, 1], s=50, c='blue', label='Cluster 2')
plt.scatter(X_scaled[clusters == 2, 0], X_scaled[clusters == 2, 1], s=50, c='green', label='Cluster 3')
plt.scatter(X_scaled[clusters == 3, 0], X_scaled[clusters == 3, 1], s=50, c='cyan', label='Cluster 4')
plt.scatter(X_scaled[clusters == 4, 0], X_scaled[clusters == 4, 1], s=50, c='magenta', label='Cluster 5')
# visualizzazione dei centroidi
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='yellow', label='Centroidi')
plt.title('Cluster di Clienti')
plt.xlabel('Reddito Annuale (scalato)')
plt.ylabel('Punteggio di Spesa (scalato)')
plt.legend()
plt.show()

# 6. ANALISI DEI CLUSTER
# Analisi delle caratteristiche dei cluster
cluster_analysis = df.groupby('Cluster').agg({
    'RedditoAnnuo': ['mean', 'median'],
    'IndicediSpesa': ['mean', 'median'],
    'IDCliente': 'count'
}).rename(columns={'CustomerID': 'Count'})

print(cluster_analysis)