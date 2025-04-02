"""
Nome Script: nuovo_archiviolibri.py
Descrizione: Questo script crea un archivio di libri con funzionalità di filtro, aggiunta, modifica ed eliminazione dei libri. 
Utilizza tkinter per l'interfaccia grafica e PIL per la gestione delle immagini. Si appoggia su un database CSV per il salvataggio dei dati.
Autore: Antonio Napolitano
Versione: 1.1
Data: 02/04/2025
Copyright: © Antonio Napolitano 2025
Licenza: MIT
"""


import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, filedialog
from PIL import Image, ImageTk
import csv
import os

class ArchivioLibri:
    def __init__(self, root):
        self.root = root
        self.root.title("Archivio Libri")
        self.libri = []
        self.crea_interfaccia()
        self.carica_dati_csv("archivio.csv")

    def carica_dati_csv(self, nome_file):
        if os.path.exists(nome_file):
            try:
                with open(nome_file, "r", newline="", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    self.libri = list(reader)
                    for libro in self.libri:
                        libro["prezzo"] = float(libro["prezzo"])
            except Exception as e:
                messagebox.showerror("Errore", f"Errore durante il caricamento del file CSV: {e}")
            self.aggiorna_lista_libri(self.libri)
        else:
            messagebox.showinfo("Info", "File CSV non trovato. Inizializzando un archivio vuoto.")

    def salva_dati_csv(self, nome_file):
        try:
            with open(nome_file, "w", newline="", encoding="utf-8") as file:
                campi = ["titolo", "autore", "prezzo", "disponibilità", "copertina"]
                writer = csv.DictWriter(file, fieldnames=campi)
                writer.writeheader()
                writer.writerows(self.libri)
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante il salvataggio del file CSV: {e}")

    def crea_interfaccia(self):
        # Frame per i filtri
        filtri_frame = ttk.LabelFrame(self.root, text="Filtri")
        filtri_frame.pack(padx=10, pady=10, fill="x")

        # Filtro per titolo
        ttk.Label(filtri_frame, text="Titolo:").grid(row=0, column=0, padx=5, pady=5)
        self.titolo_filtro = ttk.Entry(filtri_frame)
        self.titolo_filtro.grid(row=0, column=1, padx=5, pady=5)

        # Filtro per autore
        ttk.Label(filtri_frame, text="Autore:").grid(row=1, column=0, padx=5, pady=5)
        self.autore_filtro = ttk.Entry(filtri_frame)
        self.autore_filtro.grid(row=1, column=1, padx=5, pady=5)

        # Filtro per prezzo
        ttk.Label(filtri_frame, text="Prezzo massimo:").grid(row=2, column=0, padx=5, pady=5)
        self.prezzo_filtro = ttk.Entry(filtri_frame)
        self.prezzo_filtro.grid(row=2, column=1, padx=5, pady=5)

        # Pulsante per applicare i filtri
        ttk.Button(filtri_frame, text="Applica Filtri", command=self.applica_filtri).grid(row=3, column=0, columnspan=2, pady=10)

        # Pulsante per resettare i filtri
        ttk.Button(filtri_frame, text="Resetta Filtri", command=self.reset_filtri).grid(row=3, column=2, columnspan=2, pady=10)

        # Treeview per visualizzare i libri
        self.tree = ttk.Treeview(self.root, columns=("titolo", "autore", "prezzo", "disponibilità", "copertina"), show="headings")
        self.tree.heading("titolo", text="Titolo")
        self.tree.heading("autore", text="Autore")
        self.tree.heading("prezzo", text="Prezzo")
        self.tree.heading("disponibilità", text="Disponibilità")
        self.tree.heading("copertina", text="Copertina")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Frame per i pulsanti
        pulsanti_frame = ttk.LabelFrame(self.root, text="Azioni")
        pulsanti_frame.pack(pady=10, padx=10, fill="x")

        # Pulsante per aggiungere libri
        ttk.Button(pulsanti_frame, text="Aggiungi Libro", command=self.aggiungi_libro).grid(row=0, column=0, padx=5, pady=5)

        # Pulsante per modificare libri
        ttk.Button(pulsanti_frame, text="Modifica Libro", command=self.modifica_libro).grid(row=0, column=1, padx=5, pady=5)

        # Pulsante per eliminare libri
        ttk.Button(pulsanti_frame, text="Elimina Libro", command=self.elimina_libro).grid(row=0, column=2, padx=5, pady=5)

        # Frame per l'immagine di copertina
        self.copertina_frame = ttk.Frame(self.root)
        self.copertina_frame.pack(pady=10)

        # Etichetta per l'immagine di copertina
        self.copertina_label = ttk.Label(self.copertina_frame)
        self.copertina_label.pack()

        # Associa la funzione mostra_copertina all'evento di selezione del Treeview
        self.tree.bind("<ButtonRelease-1>", self.mostra_copertina)

    def applica_filtri(self):
        titolo_filtro = self.titolo_filtro.get().lower()
        autore_filtro = self.autore_filtro.get().lower()
        prezzo_filtro = self.prezzo_filtro.get()

        libri_filtrati = self.libri[:]

        if titolo_filtro:
            libri_filtrati = [libro for libro in libri_filtrati if titolo_filtro in libro["titolo"].lower()]

        if autore_filtro:
            libri_filtrati = [libro for libro in libri_filtrati if autore_filtro in libro["autore"].lower()]

        if prezzo_filtro:
            try:
                prezzo_massimo = float(prezzo_filtro)
                libri_filtrati = [libro for libro in libri_filtrati if libro["prezzo"] <= prezzo_massimo]
            except ValueError:
                pass

        self.aggiorna_lista_libri(libri_filtrati)

    def aggiorna_lista_libri(self, libri):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for libro in libri:
            self.tree.insert("", "end", values=(libro["titolo"], libro["autore"], libro["prezzo"], libro.get("disponibilità", "Sì"), libro.get("copertina", "")))

    def aggiungi_libro(self):
        self.root.attributes('-topmost', True) # Mantiene la finestra principale in primo piano

        titolo = simpledialog.askstring("Aggiungi Libro", "Titolo:", parent=self.root)
        if titolo is None:
            self.root.attributes('-topmost', False)
            return

        autore = simpledialog.askstring("Aggiungi Libro", "Autore:", parent=self.root)
        if autore is None:
            self.root.attributes('-topmost', False)   
            return
        
        prezzo = simpledialog.askfloat("Aggiungi Libro", "Prezzo:", parent=self.root)
        if prezzo is None:
            self.root.attributes('-topmost', False)
            return
        
        disponibilita = simpledialog.askstring("Aggiungi Libro", "Disponibilità (Sì/No):", initialvalue="Sì", parent=self.root)
        if disponibilita is None:
            self.root.attributes('-topmost', False)
            return
        copertina = filedialog.askopenfilename(title="Seleziona immagine copertina", filetypes=(("Immagini JPG", "*.jpg"), ("Immagini PNG", "*.png"), ("Tutti i file", "*.*")), parent=self.root)
        if copertina is None:
            self.root.attributes('-topmost', False)
            return
        self.root.attributes('-topmost', False) # Ripristina la finestra principale

        if titolo and autore and prezzo is not None:
            nuovo_libro = {"titolo": titolo, "autore": autore, "prezzo": prezzo, "disponibilità": disponibilita, "copertina": copertina}
            for libro in self.libri:
                if libro["titolo"] == titolo and libro["autore"] == autore:
                    messagebox.showerror("Errore", "Il libro esiste già.")
                    return
            self.libri.append(nuovo_libro)
            self.aggiorna_lista_libri(self.libri)
            self.salva_dati_csv("archivio.csv")
        else:
            messagebox.showerror("Errore", "Dati libro non validi.")

    def modifica_libro(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            titolo, autore, prezzo, disponibilita, copertina = item["values"]

            nuovo_titolo = simpledialog.askstring("Modifica Libro", "Nuovo Titolo:", initialvalue=titolo)
            nuovo_autore = simpledialog.askstring("Modifica Libro", "Nuovo Autore:", initialvalue=autore)
            nuovo_prezzo = simpledialog.askfloat("Modifica Libro", "Nuovo Prezzo:", initialvalue=float(prezzo))
            nuova_disponibilita = simpledialog.askstring("Modifica Libro", "Nuova Disponibilità (Sì/No):", initialvalue=disponibilita)
            nuova_copertina = filedialog.askopenfilename(title="Seleziona immagine copertina", filetypes=(("Immagini JPG", "*.jpg"), ("Immagini PNG", "*.png"), ("Tutti i file", "*.*")))

            if nuovo_titolo and nuovo_autore and nuovo_prezzo is not None:
                for libro in self.libri:
                    if libro["titolo"] == titolo and libro["autore"] == autore and libro["prezzo"] == float(prezzo):
                        libro["titolo"] = nuovo_titolo
                        libro["autore"] = nuovo_autore
                        libro["prezzo"] = nuovo_prezzo
                        libro["disponibilità"] = nuova_disponibilita
                        libro["copertina"] = nuova_copertina
                        break

                self.aggiorna_lista_libri(self.libri)
                self.salva_dati_csv("archivio.csv")
            else:
                messagebox.showerror("Errore", "Dati libro non validi.")
        else:
            messagebox.showwarning("Selezione", "Seleziona un libro da modificare.")

    def elimina_libro(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            titolo, autore, prezzo, disponibilita, copertina = item["values"]

            self.libri = [libro for libro in self.libri if not (libro["titolo"] == titolo and libro["autore"] == autore and libro["prezzo"] == float(prezzo) and libro["disponibilità"] == disponibilita and libro["copertina"] == copertina)]

            self.aggiorna_lista_libri(self.libri)
            self.salva_dati_csv("archivio.csv")
        else:
            messagebox.showwarning("Selezione", "Seleziona un libro da eliminare.")

    def reset_filtri(self):
        self.titolo_filtro.delete(0, tk.END)
        self.autore_filtro.delete(0, tk.END)
        self.prezzo_filtro.delete(0, tk.END)
        self.aggiorna_lista_libri(self.libri)

    def mostra_copertina(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            copertina_path = item["values"][4]  # Indice della colonna "copertina"

            if copertina_path:
                try:
                    image = Image.open(copertina_path)
                    image.thumbnail((200, 200))  # Ridimensiona l'immagine
                    photo = ImageTk.PhotoImage(image)
                    self.copertina_label.config(image=photo)
                    self.copertina_label.image = photo
                except Exception as e:
                    messagebox.showerror("Errore", f"Impossibile caricare l'immagine: {e}")
            else:
                self.copertina_label.config(image="")
                self.copertina_label.image = None

if __name__ == "__main__":
    root = tk.Tk()
    archivio = ArchivioLibri(root)
    root.mainloop()