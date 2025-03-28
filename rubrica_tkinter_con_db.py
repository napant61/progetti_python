"""
Nome Script: rubrica_tkinter_database.py
Descrizione: Una rubrica telefonica con interfaccia tkinter che permette
di aggiungere, modificare, elimiinare e visualizzare i contatti salvandoli al contempo in un semplice database sqlite. Il programma è stato costruito
in due fasi: prima con l'utilizzo di semplici finestre di dialogo prese dalla libreria messagebox e successivamente tramite la libreria più
sofisticata di ttk. 
Autore: Antonio Napolitano
Versione: 1.1
Data: 28/03/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""

# importare le librerie necessarie
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# creazione del database
conn = sqlite3.connect("rubrica.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS contatti (nome TEXT, numero TEXT)")
conn.commit()
conn.close()

# funzione per salvare il contatto nel database
def salva_contatto():
    nome = tk_nome.get()
    numero = tk_numero.get()
    if nome and numero:
        conn = sqlite3.connect("rubrica.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contatti (nome, numero) VALUES (?, ?)", (nome, numero))
        conn.commit()
        conn.close()
        messagebox.showinfo("Successo", f"Contatto {nome} salvato correttamente")
        aggiorna_treeview()
    else:
        messagebox.showerror("Errore", "Inserisci un nome e un numero")

# funzione per visualizzare i contatti salvati
def visualizza_contatti():
    conn = sqlite3.connect("rubrica.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatti")
    records = cursor.fetchall()
    conn.close()

    if records:
        contatti_str = "\n".join([f"{nome}: {numero}" for nome, numero in records])
        messagebox.showinfo("Rubrica", contatti_str)
    else:
        messagebox.showinfo("Rubrica", "Rubrica vuota")


# funzione per cercare un contatto della rubrica
def cerca_contatto():
    nome = tk_nome_cerca.get()
    conn = sqlite3.connect("rubrica.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatti WHERE nome=?", (nome,))
    record = cursor.fetchone()
    conn.close()

    if record:
        tk_numero_cerca.config(state="normal")
        tk_numero_cerca.delete(0, tk.END)
        tk_numero_cerca.insert(0, record[1])
        tk_numero_cerca.config(state="readonly")
        
    else:
        messagebox.showerror("Errore", f"Contatto {nome} non trovato")
    
# funzione per eliminare un contatto ma solo se i campi nome e numero sono stati compilati e il contatto esiste nel database
def elimina_contatto():
    nome = tk_nome.get()
    numero = tk_numero.get()
    if nome and tk_numero.get():
        conn = sqlite3.connect("rubrica.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contatti WHERE nome=? AND numero=?", (nome, numero))
        conn.commit()
        conn.close()
        messagebox.showinfo("Successo", f"Contatto {nome} eliminato correttamente")
        aggiorna_treeview()
    else:
        messagebox.showerror("Errore", "Inserisci un nome e un numero")

# funzione per modificare un contatto ma solo se i campi nome e numero sono stati compilati e il contatti esiste nel database
def modifica_contatto():
    nome = tk_nome.get()
    numero = tk_numero.get()
    if nome and numero:
        conn = sqlite3.connect("rubrica.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE contatti SET numero=? WHERE nome=?", (numero, nome))
        conn.commit()
        conn.close()
        messagebox.showinfo("Successo", f"Contatto {nome} modificato correttamente")
        aggiorna_treeview()
    else:
        messagebox.showerror("Errore", "Inserisci un nome e un numero")
    
# funzione per resettare tutti i campi di input
def reset():
    tk_nome.delete(0, tk.END)
    tk_numero.delete(0, tk.END)
    tk_nome_cerca.delete(0, tk.END)
    tk_numero_cerca.config(state="normal")
    tk_numero_cerca.delete(0, tk.END)
    tk_numero_cerca.config(state="readonly")


# creare il layout della finestra
root = tk.Tk()
root.title("Rubrica Telefonica")
root.geometry("600x700")    

# creare un frame per i campi di input
campi_frame = ttk.LabelFrame(root, text="Inserisci Contatto")
campi_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# creare le labels e i campi di input per il nome e il numero
tk.Label(campi_frame, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
tk_nome = tk.Entry(campi_frame)
tk_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(campi_frame, text="Numero:").grid(row=1, column=0, padx=10, pady=10)
tk_numero = tk.Entry(campi_frame)
tk_numero.grid(row=1, column=1, padx=10, pady=10)

# creare un frame per i pulsanti
pulsanti_frame = ttk.LabelFrame(root, text="Operazioni")
pulsanti_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# creare i pulsanti per le operazioni
# pulsante per salvare il contatto
btn_salva = ttk.Button(pulsanti_frame, text="Salva", command=salva_contatto)
btn_salva.grid(row=0, column=0, padx=10, pady=10)

# pulsante per visualizzare i contatti
btn_visualizza = ttk.Button(pulsanti_frame, text="Visualizza Contatti", command=visualizza_contatti)
btn_visualizza.grid(row=0, column=1, padx=10, pady=10)

# pulsante per eliminare un contatto
btn_elimina = ttk.Button(pulsanti_frame, text="Elimina Contatto", command=elimina_contatto)
btn_elimina.grid(row=0, column=2, padx=10, pady=10)

# pulsante per modificare un contatto
btn_modifica = ttk.Button(pulsanti_frame, text="Modifica Contatto", command=modifica_contatto)
btn_modifica.grid(row=0, column=3, padx=10, pady=10)

# creare un frame per visualizzare i contatti
contatti_frame = ttk.LabelFrame(root, text="Contatti")
contatti_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# creare un frame per cercare un contatto
cerca_frame = ttk.LabelFrame(root, text="Cerca Contatto")
cerca_frame.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# creare i pulsanti per cercare un contatto
tk.Label(cerca_frame, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
tk_nome_cerca = tk.Entry(cerca_frame)
tk_nome_cerca.grid(row=0, column=1, padx=10, pady=10)
btn_cerca = ttk.Button(cerca_frame, text="Cerca", command=cerca_contatto)
btn_cerca.grid(row=0, column=2, padx=10, pady=10)
tk_numero_cerca = tk.Entry(cerca_frame, state="readonly")
tk_numero_cerca.grid(row=0, column=3, padx=10, pady=10)

# creare il pulsante di reset
btn_reset = ttk.Button(root, text="Reset", command=reset)
btn_reset.grid(row=4, column=0, padx=10, pady=10)


# creare una treeview per visualizzare i contatti
tree = ttk.Treeview(contatti_frame, columns=("Nome", "Numero"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Numero", text="Numero")
tree.pack(padx=10, pady=10, fill="both", expand=True)

# funzione per aggiornare la treeview
def aggiorna_treeview():
    for i in tree.get_children():
        tree.delete(i)

    conn = sqlite3.connect("rubrica.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatti")
    records = cursor.fetchall()
    conn.close()

    for record in records:
        tree.insert("", "end", values=record)

aggiorna_treeview()

# funzione per mostrare il contatto selezionato della treeview nei campi tk_nome.get()e e tk_numeroe.get()
def seleziona_contatto(event):
    selected_items = tree.selection()
    if selected_items:  # Controlla se c'è almeno un elemento selezionato
        selected_item = selected_items[0]
        contatto = tree.item(selected_item, "values")
        tk_nome.delete(0, tk.END)
        tk_nome.insert(0, contatto[0])
        tk_numero.delete(0, tk.END)
        tk_numero.insert(0, contatto[1])
    else:
        # Nessuna selezione, puoi gestire il caso se necessario
        pass

# associare l'evento di selezione alla funzione seleziona_contatto
tree.bind("<<TreeviewSelect>>", seleziona_contatto)

# avviare il loop principale dell'interfaccia grafica


root.mainloop()