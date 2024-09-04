entree = """10
1 8
3 4
8 3
2 3
2 6
7 6
5 6
5 9
6 0"""

entree = entree.split("\n")

index = 0
def readline():
    global index, entree
    index += 1
    return entree[index-1]

import sys
sys.setrecursionlimit(10**4)
sys.stdin.readline = readline
input = readline

### copier en-dessous
import sys
n = int(input())

sortant = [[] for i in range(n)]
taille_branche_plus_longue = [0 for i in range(n)]
deja_visite = [0 for i in range(n)] # 0, 1, 2 => blanc, gris, noir

mini = n # on devra ensuite choisir le minimum parmi les maximums


## Construction de l'arbre
for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    sortant[a].append(b)
    sortant[b].append(a)


## Fonctions
def explore(noeud):
    global compteur, i, j

    if i == 5 and j == 6:
        print("coucou frérot")
        print(deja_visite)

    compteur += 1
    deja_visite[noeud] = 1

    for k in sortant[noeud]:
        if deja_visite[k] == 0:
            if i == 5 and j == 6:
                print("j'explore le noeud", k)
            explore(k)

    deja_visite[noeud] = 0

## Programme
for i in range(n):
    maxi = taille_branche_plus_longue[i]
    print("\n-------------------------\nnoeud numéro", i)
    deja_visite[i] = 1

    for j in sortant[i]:
        print("\n-----\nvoisin", j)
        compteur = 0
        if len(sortant[i]) == 1:
            maxi = n-1 # pas besoin de parcourir si le noeud est une feuille
            #taille_branche_plus_longue[j] = n - maxi # pas bon
        elif deja_visite[j] == 0:
            explore(j)
            print("compteur", compteur, "et maxi", maxi)
            maxi = max(compteur, maxi)
            print("taille j", j, "n - compteur", n - compteur)
            taille_branche_plus_longue[j] = max(n - compteur, taille_branche_plus_longue[j])

    deja_visite[i] = 0


    taille_branche_plus_longue[i] = maxi


        # ensuite donner le maxi à la branche d'à côté de la forme n - maxi



print(min(taille_branche_plus_longue))