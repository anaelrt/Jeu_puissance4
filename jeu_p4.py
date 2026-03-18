

import random                                        #ordre du joueur
ordre_joueur=random.randint(1, 2)
print(ordre_joueur)
if ordre_joueur == 1:
    print("tu commences")
else:
    print("tu ne commences pas à jouer en premier")

if ordre_joueur == 1:           #assignation des pions aux joueurs
    ordre_joueur="O"
    print("tu as les pions O")
else:
    ordre_joueur ="X"
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
    return ligne

print(affiche_matrice(matrice))



#def addToken(joueur, colonne):