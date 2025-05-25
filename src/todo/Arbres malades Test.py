entree = """6 3
7 4 4
5 3 2
2 3 0
6 7 1
3 7 3
5 2 3
4
0
2"""

entree = """5 3
7 4 4
5 3 2
2 3 0
6 7 1
3 7 3
4
0
2"""

entree = """5 36
7 4 54
5 3 52
2 3 50
6 7 51
3 7 53
0
1
2
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4"""

entree = entree.split("\n")

index = 0


def readline():
    global index, entree
    index += 1
    return entree[index - 1]


import sys

sys.setrecursionlimit(10**4)
sys.stdin.readline = readline
input = readline

### copier en-dessous
import sys
from collections import deque

sys.setrecursionlimit(10**8)
n, m = map(int, input().split())


### Variables
arbres = [[] for i in range(n)]
arbres_a_cote = [[] for i in range(n)]
deja_visite = [0 for i in range(n)]
nb_arbres_contamines = [-1 for i in range(n)]  # on stocke les résultats
# si on demande plusieurs fois le même arbre


### Fonctions
def distance(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


### Traitement des données
for i in range(n):
    x, y, r = map(int, sys.stdin.readline().split())
    arbres[i] = (x, y, r**2)

for i in range(n):
    x1, y1, r = arbres[i]
    for j in range(n):
        x2, y2, _ = arbres[j]  # "_" est ignoré
        if distance(x1, y1, x2, y2) <= r:
            arbres_a_cote[i].append(j)


### Programme
for i in range(m):
    compteur = 0
    arbre_a_test = int(sys.stdin.readline())

    if nb_arbres_contamines[arbre_a_test] == -1:
        file = deque([arbre_a_test])
        deja_visite[arbre_a_test] = i

        while file:
            noeud = file.popleft()

            compteur += 1

            for _, noeud_actif in enumerate(arbres_a_cote[noeud]):
                if deja_visite[noeud_actif] != i:
                    deja_visite[noeud_actif] = i
                    file.append(noeud_actif)

        nb_arbres_contamines[arbre_a_test] = compteur

    print(nb_arbres_contamines[arbre_a_test])
