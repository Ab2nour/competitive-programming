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
    return entree[index - 1]


import sys

sys.setrecursionlimit(10**4)
sys.stdin.readline = readline
input = readline

### copier en-dessous
import sys

## ---------- Entrées / données ----------
nb_noeuds, nb_aretes = map(int, sys.stdin.readline().split())

aretes = [None for i in range(nb_aretes)]
deja_vu = [False for i in range(nb_aretes)]

indispensable = [True for i in range(nb_aretes)]

voisins = [[] for i in range(nb_noeuds + 1)]
profondeur = [-1 for i in range(nb_noeuds + 1)]


for i in range(nb_aretes):
    a, b = map(int, sys.stdin.readline().split())

    aretes[i] = (a, b)
    voisins[a].append((b, i))
    voisins[b].append((a, i))


## ---------- Fonctions ----------
def profondeur_min(noeud, prof):
    if profondeur[noeud] != -1:
        return profondeur[noeud]

    profondeur[noeud] = prof
    prof_min = prof

    for i, id_arete in voisins[noeud]:
        if not deja_vu[id_arete]:
            deja_vu[id_arete] = True

            prof_trouvee = profondeur_min(i, prof + 1)
            prof_min = min(prof_min, prof_trouvee)

            indispensable[id_arete] = prof_trouvee > prof

    return prof_min


## ---------- Affichage ----------
profondeur_min(1, 0)

ponts = [aretes[i] for i in range(nb_aretes) if indispensable[i]]

ponts.sort()

print(len(ponts))


for a, b in ponts:
    print(a, b)
