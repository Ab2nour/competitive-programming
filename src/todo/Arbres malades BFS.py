import sys
from collections import deque

sys.setrecursionlimit(10**8)
n, m = map(int, input().split())


### Variables
arbres = [[] for i in range(n)]
arbres_a_cote = [[] for i in range(n)]
deja_visite = [False for i in range(n)]
nb_arbres_contamines = [-1 for i in range(n)] # on stocke les résultats
                                # si on demande plusieurs fois le même arbre


### Fonctions
def distance(x1, y1, x2, y2):
    return (x2-x1)**2 + (y2-y1)**2


### Traitement des données
for i in range(n):
    x, y, r = map(int, sys.stdin.readline().split())
    arbres[i] = (x, y, r**2)

for i in range(n):
    x1, y1, r = arbres[i]
    for j in range(n):
        x2, y2, _ = arbres[j] # "_" est ignoré
        if i != j and distance(x1, y1, x2, y2) <= r:
            arbres_a_cote[i].append(j)


### Programme
for i in range(m):
    compteur = 0
    arbre_a_test = int(sys.stdin.readline())

    if nb_arbres_contamines[arbre_a_test] == -1:
        file = deque([arbre_a_test])
        deja_visite[arbre_a_test] = True

        while file:
            noeud = file.popleft()

            compteur += 1

            for _, noeud_actif in enumerate(arbres_a_cote[noeud]):
                if not deja_visite[noeud_actif]:
                    deja_visite[noeud_actif] = True
                    file.append(noeud_actif)

        nb_arbres_contamines[arbre_a_test] = compteur
        deja_visite = [False for i in range(n)]

    print(nb_arbres_contamines[arbre_a_test])