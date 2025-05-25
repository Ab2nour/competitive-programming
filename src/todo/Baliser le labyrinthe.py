entree = """12 20
1 2
1 3
2 3
2 4
2 5
3 5
3 7
4 6
5 6
5 7
6 7
6 8
6 10
6 11
7 8
8 9
8 10
9 10
10 12
11 12"""

entree = entree.split("\n")

index = 0


def readline():
    global index, entree
    index += 1
    return entree[index - 1]


import sys

sys.stdin.readline = readline
input = readline

### copier en-dessous
import sys

## Données
nb_sommets, nb_aretes = map(int, input().split())

voisins = [[] for i in range(nb_sommets + 1)]
deja_vu_sommet = [0 for i in range(nb_sommets + 1)]  # pour les sommets

nb_sommets_a_voir = nb_sommets

aretes = []
deja_vu_arete = [False for i in range(nb_aretes)]  # pour les arêtes

chemin = []
chemin_en_cours = []
noeud_depart = 1
deuxieme_passage = False


## Fonctions
def noeud_non_libre(n):
    """Détermine si le noeud n est non libre, c'est-à-dire s'il ne lui reste
    plus d'arêtes non visitées.
    Donc on a vu ce sommet autant de fois qu'il a d'arêtes."""
    return deja_vu_sommet[n] == len(voisins[n])


def parcours(n):
    global nb_sommets_a_voir, deuxieme_passage
    # print(n)

    chemin_en_cours.append(n)

    # n est le noeud de départ
    if n == noeud_depart:
        if deuxieme_passage:  # on est revenu au point de départ yes !
            if noeud_non_libre(n):
                nb_sommets_a_voir -= 1

            return

        else:
            deuxieme_passage = True

    # parcours des voisins
    for i in range(len(voisins[n])):
        voisin = voisins[n][i][0]
        arete = voisins[n][i][1]

        if not deja_vu_arete[arete]:
            deja_vu_arete[arete] = True

            deja_vu_sommet[n] += 1
            deja_vu_sommet[voisin] += 1

            parcours(voisin)
            break

    if noeud_non_libre(n):
        nb_sommets_a_voir -= 1

    return


for i in range(nb_aretes):
    a, b = map(int, input().split())

    voisins[a].append((b, i))
    voisins[b].append((a, i))

    aretes.append((a, b))


# Vérification si le parcours est possible
for i in range(1, nb_sommets):
    if len(voisins[i]) % 2:
        print(-1)
        exit()


# Sommets isolés
while len(voisins[noeud_depart]) == 0:
    noeud_depart += 1


chemin.append(1)
noeud_a_explorer = 1
pos_noeud = 0

while nb_sommets_a_voir > 0:  # WHILE 1 : tant qu'il y a des sommets libres
    deuxieme_passage = False
    parcours(noeud_depart)

    # chemin = chemin[:pos_noeud] + chemin_en_cours + chemin[pos_noeud+1:]
    chemin = (
        [chemin[i] for i in range(pos_noeud)]
        + chemin_en_cours
        + [chemin[i] for i in range(pos_noeud + 1, len(chemin))]
    )

    chemin_en_cours = []
    # mettre à jour le noeud de départ (le prendre dans le chemin)
    while pos_noeud < len(chemin):
        if not noeud_non_libre(chemin[pos_noeud]):  # le noeud est libre
            noeud_depart = chemin[pos_noeud]
            break

        pos_noeud += 1


for i in chemin:
    print(i, end=" ")
