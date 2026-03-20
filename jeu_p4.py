

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

m=6    #matrice de depart
n=7
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

affichage_matrice(matrice)


choix_colonne=int(input("dans quelle colonne voulez vous mettre le pion ? "))   #ca fonctionne pas
while choix_colonne<0 or choix_colonne>6:
    print("cette colonne est inexistante")
    choix_colonne=int(input("ecrire une colonne entre 0 et 6 : "))
else:
    for i in range(43):
        while choix_colonne == " ":
            if ordre_joueur == 1:
                matrice.append("O")
            else:
                matrice.append("X")

            





#def addToken(joueur, colonne):
