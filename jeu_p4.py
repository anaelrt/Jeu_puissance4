"jeu_p4"
#a=2
#b=3
#c=4
#d=5


m=int(input("nombre de lignes"))
n=int(input("nombre de colonnes"))
matrice=[]
for ligne_index in range(m):
    ligne=[]
    for colonne_index in range(n):
        valeur=int(input())
        ligne.append(valeur)
    matrice.append(ligne)


def addToken(joueur, colonne):
    pass


