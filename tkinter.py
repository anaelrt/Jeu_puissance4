import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
label1 = tk.Label(racine, text="Un texte long dans ma fenêtre", font = ("helvetica", "30")) # création d'un widget
label2 = tk.Label(racine, text="toto",font = ("helvetica", "30")) # création d'un widget
label1.grid(column=0, row=0, padx=50) # positionnement du premier widget
label2.grid(column=0, row=1, pady=10) # positionnement du premier widget
racine.mainloop() # Lancement de la boucle principale
