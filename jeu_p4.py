

import random                                        #choix de l'ordre du joueur
choix_joueur=random.randint(1, 2)
print(choix_joueur)
if choix_joueur == 1:
    print("tu commences")
else:
    print("tu ne commences pas à jouer en premier")


m=int(input("nombre de lignes"))
n=int(input("nombre de colonnes"))
matrice=[]
for ligne_index in range(m):
    ligne=[]
    for colonne_index in range(n):
        valeur=int(input())
        ligne.append(valeur)
    matrice.append
    matrice.append(ligne)


def addToken(joueur, colonne):
#test
#print("--Puissance--")