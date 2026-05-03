import tkinter as tk
import random

tab1=[]
tab2=[]

joueur1=input("nom du joueur 1 : ")
joueur2=input("nom du joueur 2 : ")

m=int(input("nombre de lignes : "))
n=int(input("nombre de colonnes : "))

couleur_j1="yellow"
couleur_j2="red"

                                    #ordre du joueur
ordre_joueur=random.randint(1, 2)
print("le joueur qui commence est le joueur ", ordre_joueur)

if ordre_joueur==1:               #assignation des pions aux joueurs
    joueur_actuel=couleur_j1
else:
    joueur_actuel=couleur_j2     


def creation_matrice():
    matrice=[]
    for ligne_index in range(m):
        ligne=[]
        for colonne_index in range(n):
            valeur=str(' ')
            ligne.append(valeur)
        matrice.append(ligne)
    return matrice

matrice=creation_matrice()

label_victoire=None
partie_terminee=False


def enregistrer_partie(joueur_actuel, colonne_index):       #enregistre les coups des joueurs
    if joueur_actuel==couleur_j1:
        tab1.append(colonne_index)
    else:
        tab2.append(colonne_index)


def victoire(matrice):            #verif si il y a victoire
    m = len(matrice)        # nombre de lignes
    n = len(matrice[0])     # nombre de colonnes

    # horizontal 
    for i in range(m):
        for j in range(n - 3):
            if (matrice[i][j] != " " and
                matrice[i][j] == matrice[i][j+1] == matrice[i][j+2] == matrice[i][j+3]):
                return matrice[i][j]

    # vertical
    for i in range(m - 3):
        for j in range(n):
            if (matrice[i][j] != " " and
                matrice[i][j] == matrice[i+1][j] == matrice[i+2][j] == matrice[i+3][j]):
                return matrice[i][j]

    # diagonale vers le bas
    for i in range(m - 3):
        for j in range(n - 3):
            if (matrice[i][j] != " " and
                matrice[i][j] == matrice[i+1][j+1] == matrice[i+2][j+2] == matrice[i+3][j+3]):
                return matrice[i][j]

    # diagonale vers le haut
    for i in range(3, m):
        for j in range(n - 3):
            if (matrice[i][j] != " " and
                matrice[i][j] == matrice[i-1][j+1] == matrice[i-2][j+2] == matrice[i-3][j+3]):
                return matrice[i][j]

        
    return None  # pas de gagnant              


def file():        #enregistrer les coups dans tab1et tab2 du fichier 
    file=open("jeu_p4.txt", "w")          
    file.write("coups du joueur1 : " + str(tab1) + "\n")
    file.write("Coups du joueur2 : " + str(tab2) + "\n") 
    file.close()


taille=90

fenetre=tk.Tk()               #tkinter
fenetre.title("PUISSANCE 4")
fenetre.geometry("1500x1500")
fenetre["bg"]="blue"

canvas=tk.Canvas(fenetre, background="blue", height=m*taille, width=n*taille)
canvas.grid(row=2, column=0, columnspan=3, padx=40, pady=50)


def dessin_matrice():          #dessin de la grille 
    canvas.delete("all")
    for ligne_index in range(m):
        for colonne_index in range(n):
            x0=colonne_index*taille
            y0=ligne_index*taille
            x1=x0+taille
            y1=y0+taille

            if matrice[ligne_index][colonne_index]==" ":
                couleur="white"
            elif matrice[ligne_index][colonne_index]=="yellow":
                couleur="yellow"
            else:
                couleur="red"

            canvas.create_oval(x0, y0, x1, y1, fill=couleur, outline="black", width=2)
dessin_matrice()


def jouer(colonne_index):        #mettre le pion dans le plus bas de la colonne
    global joueur_actuel, label_victoire, partie_terminee
    if partie_terminee:
        return 
    for ligne_index in range(m-1, -1, -1):
        if matrice[ligne_index][colonne_index]==" ":
            matrice[ligne_index][colonne_index]=joueur_actuel
            enregistrer_partie(joueur_actuel, colonne_index)
            break
    else:
        return "la colonne est pleine"
    dessin_matrice()

    gagnant=victoire(matrice)    #affichage du gagnant
    if gagnant:
        if gagnant==couleur_j1:
            nom_gagnant=joueur1
        else:
            nom_gagnant=joueur2
        label_victoire=tk.Label(fenetre, text=f"Victoire de {nom_gagnant}", background="purple", foreground="pink", font=("Arial", 40))
        label_victoire.grid(column=0, row=2, columnspan=3, pady=50)
        file()
        partie_terminee=True
        return
    

    if joueur_actuel==couleur_j1:     #alternance des joueurs
        joueur_actuel=couleur_j2
    else:
        joueur_actuel=couleur_j1


def clic(event):     #permet de clic pour deposer le pion
    if partie_terminee:
        return
    colonne=event.x//taille
    if 0<=colonne<n:
        jouer(colonne)

canvas.bind("<Button-1>", clic)


def annuler_coup():      #annuler
    global joueur_actuel
    if joueur_actuel==couleur_j2:
        if not tab1:
            return
        colonne=tab1.pop()
        joueur_actuel=couleur_j1
    else:
        if not tab2:
            return
        colonne=tab2.pop()
        joueur_actuel=couleur_j2


    for ligne_index in range(m):
        if matrice[ligne_index][colonne]!=" ":
            matrice[ligne_index][colonne]=" "
            break
    dessin_matrice()


def recommencer():        #recommencer 
    global matrice, joueur_actuel, label_victoire, partie_terminee
    matrice=creation_matrice()
    tab1.clear()
    tab2.clear()
    if ordre_joueur==1:
        joueur_actuel=couleur_j1
    else:
        joueur_actuel=couleur_j2
    if label_victoire is not None:
        label_victoire.destroy()
        label_victoire=None
    partie_terminee=False
    dessin_matrice()


        
bouton_annuler=tk.Button(fenetre, text="ANNULER LE DERNIER COUP", relief="raised", cursor="heart",  command=annuler_coup)    #bouton annuler
bouton_annuler.bind("<Button-1>")
bouton_annuler.grid(row=0, column=1, sticky="e", padx=20) 


bouton_recommencer=tk.Button(fenetre, text="RECOMMENCER UNE PARTIE", relief="raised", cursor="star",  command=recommencer)    #bouton recommencer une partie
bouton_recommencer.bind("<Button-1>")
bouton_recommencer.grid(row=0, column=2, sticky="e", padx=20) 



fenetre.grid_columnconfigure(2, weight=1)          #ajuster la taille des colonnes
fenetre.grid_rowconfigure(5, weight=5)
fenetre.mainloop()


