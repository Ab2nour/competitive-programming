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
sys.setrecursionlimit(10**9)

readline = sys.stdin.readline

n = int(input())

sortant = [[] for i in range(n)]
branche_plus_longue = [0 for i in range(n)]

compteur = [0 for i in range(n)]
deja_visite = [0 for i in range(n)] # 0, 1, 2 => blanc, gris, noir
noeuds_visites = []

minimum = 10**5+1


## Construction de l'arbre
for i in range(n-1):
    a, b = map(int, readline().split())

    sortant[a].append(b)
    sortant[b].append(a)


## Fonctions
def explore(noeud):
    global compteur, minimum

    print("\n\n\nnoeud", noeud)
    print("-----------")

    print(compteur)

    maxi = branche_plus_longue[noeud]

    deja_visite[noeud] = 1
    noeuds_visites.append(noeud)

    compteur_noeuds_visites = 0

    for k in sortant[noeud]:
        if deja_visite[k] == 0:
            compteur[noeud] = 0

            #print(noeuds_visites)
            compteur_noeuds_visites += 1

            explore(k)

            branche_plus_longue[k] = max(branche_plus_longue[k], n - compteur[noeud])
            print("branche_plus_longue", branche_plus_longue[k])
            minimum = min(minimum, branche_plus_longue[k])
            maxi = max(compteur[noeud], maxi)


    for j in noeuds_visites:
        compteur[j] += 1
    #print("roger", noeuds_visites)

    branche_plus_longue[noeud] = maxi
    noeuds_visites.pop()


## Programme
explore(0)

print(minimum)

