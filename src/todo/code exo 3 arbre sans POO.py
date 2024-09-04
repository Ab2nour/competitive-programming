import sys

N = int(input())
liste_pour_noeuds = list(map(int, input().split()))
R = int(input())

liste_noeuds_visites = [0 for i in range(N+1)]

def plus_petit_ancetre_commun(noeud1, noeud2):
    index_noeuds_visites = []
    liste_noeuds_visites[noeud1] = 1

    while noeud1 != 0:
        index_noeuds_visites.append(noeud1)
        noeud1 = liste_pour_noeuds[noeud1-1]
        liste_noeuds_visites[noeud1] = 1


    while liste_noeuds_visites[noeud2] == 0:
        noeud2 = liste_pour_noeuds[noeud2-1]
        if noeud2 == 0:
            break

    for i in index_noeuds_visites:
        liste_noeuds_visites[i] = 0

    print(noeud2)

for i in range(R):
    noeud1, noeud2 = map(int, input().split())
    plus_petit_ancetre_commun(noeud1, noeud2)

