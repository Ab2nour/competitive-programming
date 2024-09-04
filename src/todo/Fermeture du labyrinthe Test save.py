entree = """12 16
1 2
1 3
2 4
2 6
3 6
3 7
4 5
5 7
5 9
5 10
6 5
7 8
8 11
9 12
10 9
11 10"""

entree = entree.split("\n")

index = 0
def readline():
    global index, entree
    index += 1
    return entree[index-1]

import sys
N, A = map(int, readline().split())

matrice_adjacence = [[0 for i in range(N+1)] for j in range(N+1)]

rien_a_afficher = False
impossible = False

### copier le code en-dessous
def aucun_ancetre(noeud):
    for i in range(1, N+1):
        if matrice_adjacence[i][noeud] == 1:
            return False
    return True

def supprime_fils(noeud):
    liste_fils_a_visiter = []
    for i in range(1, N+1):
        if matrice_adjacence[i][0] == 1: # présence de cycle
            impossible = True
        if matrice_adjacence[noeud][i] == 1:
            matrice_adjacence[noeud][i] = 0
            if aucun_ancetre(i):
                ordre.append(i)
                matrice_adjacence[i][0] = 1 # marquage comme déjà visité
                liste_fils_a_visiter.append(i)

    for i in liste_fils_a_visiter:
        supprime_fils(i)

liste_sans_ancetre = []
ordre = []

for i in range(1, N+1):
    if aucun_ancetre(i):
        rien_a_afficher = False
        liste_sans_ancetre.append(i)

if len(liste_sans_ancetre) == 0:
    rien_a_afficher = True
else:
    for i in range(len(liste_sans_ancetre)):
        ordre.append(i)
        supprime_fils(i)

if rien_a_afficher or impossible:
    print(-1)
else:
    for i in ordre:
        sys.stdout.write("%s " %i)