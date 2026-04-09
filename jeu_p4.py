

import random                                        #ordre du joueur
ordre_joueur=random.randint(1, 2)
print(ordre_joueur)
if ordre_joueur == 1:                                #assignation des pions aux joueurs
    pion_joueur1="O"
    pion_joueur2="X"
    print("tu as les pions O")
    print("tu commences")
else:
    pion_joueur2 ="X"
    pion_joueur1="O"
    print("tu as les pions X")
    print("tu ne commences pas à jouer en premier")


joueur_actuel=pion_joueur1
tour_joueur=1

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


while True:
    print(affiche_matrice(matrice))
    choix_colonne=int(input("dans quelle colonne voulez vous mettre le pion ? "))   
    while choix_colonne<0 or choix_colonne>=n:
        print("cette colonne est inexistante")
        choix_colonne = int(input(f"donner une colonne entre 0 et {n-1} : "))

    place_pion= False
    for ligne in range(m-1, -1, -1):              #mettre le pion dans le plus bas de la colonne
        if matrice[ligne][choix_colonne]==" ":
            matrice[ligne][choix_colonne]=joueur_actuel
            place_pion= True                          #gemini
            break

    if not place_pion:
        print("la colonne est pleine")
        continue



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
    
    


    gagnant = victoire(matrice)              

    if gagnant:
        print(affiche_matrice(matrice))
        print("La partie est terminée")
        print(f"Le joueur ayant les pions {gagnant} a gagné")
        break

    if not gagnant:
        if joueur_actuel==pion_joueur1:     #changer de joueur
            joueur_actuel=pion_joueur2
        else:
            joueur_actuel=pion_joueur1

    tour_joueur=1




