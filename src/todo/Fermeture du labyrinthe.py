import sys
N, A = map(int, input().split())

matrice_adjacence = [[0 for i in range(N+1)] for j in range(N+1)]

rien_a_afficher = True

for i in range(A):
    a, b = map(int, sys.stdin.readline().split())
    matrice_adjacence[a][b] = 1

def aucun_ancetre(noeud):
    for i in range(1, N+1):
        if matrice_adjacence[i][noeud] == 1:
            return False
    return True

def supprime_fils(noeud):
    liste_fils_a_visiter = []
    for i in range(1, N+1):
        if matrice_adjacence[noeud][i] == 1:
            matrice_adjacence[noeud][i] = 0
            if aucun_ancetre(i):
                print(i, end=" ")
                liste_fils_a_visiter.append(i)

    for i in liste_fils_a_visiter:
        supprime_fils(i)


for i in range(1, N+1):
    if aucun_ancetre(i):
        rien_a_afficher = False
        print(i, end=" ")
        supprime_fils(i)


if rien_a_afficher:
    print(-1)