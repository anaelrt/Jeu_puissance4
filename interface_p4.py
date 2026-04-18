import tkinter as tk
import random

fenetre = tk.Tk()
fenetre.geometry("1600x1000")
fenetre.title("puissance 4")

label_nb_ligne=tk.Label(fenetre, text="Nombres de lignes", background="pink")        #labels
label_nb_colonne=tk.Label(fenetre, text="Nombres de colonnes", background="pink")

entry_ligne=tk.Entry(fenetre)     #champs de saisie
entry_colonne=tk.Entry(fenetre)

bouton_ok=tk.Button(fenetre, text="OK")    #bouton
bouton_ok.bind("<Button-3>")

label_nb_ligne.grid(row=0, column=0, sticky="e", padx=5, pady=5)          #placement des widgets
entry_ligne.grid(row=0, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

label_nb_colonne.grid(row=1, column=0, sticky="e", padx=5, pady=5)  
entry_colonne.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

bouton_ok.grid(row=2, column=1, sticky="e", padx=20, pady=20) 

fenetre.grid_columnconfigure(2, weight=10)          #ajuster la taille des colonnes
fenetre.grid_rowconfigure(5, weight=5)
fenetre.mainloop()


