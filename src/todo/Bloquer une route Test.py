entree = """12 15
1 2
1 3
2 4
2 5
3 5
4 6
6 7
6 10
6 11
7 8
8 9
8 10
9 10
10 11
11 12"""

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
n, a = map(int, input().split())

noeuds = [i for i in range(n+1)]
entrant = [[] for i in range(n+1)]
sortant = [[] for i in range(n+1)]
indispensable = [[] for i in range(n+1)]
deja_visite = [[] for i in range(n+1)]

profondeur = [0 for i in range(n+1)]
noeuds_en_visite = []


for i in range(a):
    n1, n2 = map(int, input().split())

    # pour le parcours on regarde les noeuds sortant
    # pour les arêtes indispensables on
    # regarde les noeuds entrants
    sortant[n1].append(n2)
    sortant[n2].append(n1)
    entrant[n2].append(n1)

    indispensable[n2].append(True)
    deja_visite[n2].append(False)


def parcours(noeud, p, noeud_avant):
    print("noeud", noeud, "profondeur", p)
    if profondeur[noeud] > 0: # déjà visité
        for i in noeuds_en_visite:
            if profondeur[i] > profondeur[noeud]:
                for j in range(len(indispensable[i])):
                    indispensable[i][j] = False
        # print(indispensable)
        # print("-------------------------------------")
    else:
        profondeur[noeud] = p
        noeuds_en_visite.append(noeud)
        deja_visite[noeud]

        for i in sortant[noeud]:
            if i != noeud_avant:
                parcours(i, p+1, noeud)

        profondeur[noeud] = 0
        noeuds_en_visite.pop()

parcours(1, 1, 0)
