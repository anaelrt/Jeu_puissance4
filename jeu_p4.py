

import random                                        #choix de l'ordre du joueur
choix_joueur=random.randint(1, 2)
print(choix_joueur)
if choix_joueur == 1:
    print("tu commences")
else:
    print("tu ne commences pas à jouer en premier")


m=6    #matrice de depart
n=7
matrice=[]
for ligne_index in range(m):
    ligne=[]
    for colonne_index in range(n):
        valeur=" "
        ligne.append(valeur)
    matrice.append
    matrice.append(ligne)

def affiche_matrice(matrice):
    for ligne in matrice:
        print(ligne)

print(affiche_matrice(matrice))



#def addToken(joueur, colonne):