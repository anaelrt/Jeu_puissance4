

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


#TEST STEEVEN 


#def addToken(joueur, colonne):
