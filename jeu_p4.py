

import random                                        #ordre du joueur
ordre_joueur=random.randint(1, 2)
print(ordre_joueur)
if ordre_joueur == 1:
    print("tu commences")
else:
    print("tu ne commences pas à jouer en premier")

if ordre_joueur == 1:           #assignation des pions aux joueurs
    pion_joueur="O"
    print("tu as les pions O")
else:
    pion_joueur ="X"
    print("tu as les pions X")

m=int(input("donner un nombre de ligne : "))    #matrice de depart
n=int(input("donner un nombre de colonne : "))
matrice=[]
for ligne_index in range(m):
    ligne=[]
    for colonne_index in range(n):
        valeur=str(' ')
        ligne.append(valeur)
    matrice.append(ligne)

def affiche_matrice(matrice):
    for ligne in matrice:
        print(ligne)

affiche_matrice(matrice)



choix_colonne=int(input("dans quelle colonne voulez vous mettre le pion ? "))   #ca fonctionne pas
while choix_colonne<0 or choix_colonne>6:
    print("cette colonne est inexistante")
    choix_colonne = int(input("Écrire une colonne entre 0 et {n-1} : "))

for ligne in range(m-1, -1, -1):   #mettre le pion dans le plus bas de la colonne
    if matrice[ligne][choix_colonne]==" ":
        matrice[ligne][choix_colonne]=pion_joueur
    print(matrice)
else:
    print("la colonne est pleine ")

tour_joueur+=1




def victoire(grille):
    m = len(grille)        # nombre de lignes
    n = len(grille[0])     # nombre de colonnes

    # --- Horizontal ---
    for i in range(m):
        for j in range(n - 3):
            if (grille[i][j] != " " and
                grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3]):
                return grille[i][j]

    # --- Vertical ---
    for i in range(m - 3):
        for j in range(n):
            if (grille[i][j] != " " and
                grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j]):
                return grille[i][j]

    # --- Diagonale ↘ ---
    for i in range(m - 3):
        for j in range(n - 3):
            if (grille[i][j] != " " and
                grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3]):
                return grille[i][j]

    # --- Diagonale ↗ ---
    for i in range(3, m):
        for j in range(n - 3):
            if (grille[i][j] != " " and
                grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] == grille[i-3][j+3]):
                return grille[i][j]

    return None   # pas de gagnant


# Test
gagnant = victoire(grille)

if gagnant:
    print("La partie est terminée")
    print(f"Le joueur ayant les pions {gagnant} a gagné")


