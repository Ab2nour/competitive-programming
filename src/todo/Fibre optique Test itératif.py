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
    return entree[index - 1]


import sys

sys.stdin.readline = readline
input = readline


### copier en-dessous
def main():
    import sys

    sys.setrecursionlimit(10**9)
    from collections import deque

    readline = sys.stdin.readline

    n = int(input())

    sortant = [[] for i in range(n)]
    branche_plus_longue = [0 for i in range(n)]

    compteur = [0 for i in range(n)]
    deja_visite = [0 for i in range(n)]  # 0, 1, 2 => blanc, gris, noir
    noeuds_visites = deque()

    minimum = 10**5 + 1

    ## Construction de l'arbre
    for i in range(n - 1):
        a, b = map(int, readline().split())

        sortant[a].append(b)
        sortant[b].append(a)

    ## Fonctions
    def explore(noeud):
        nonlocal compteur, minimum

        maxi = branche_plus_longue[noeud]

        deja_visite[noeud] = 1
        noeuds_visites.append(noeud)

        for k in sortant[noeud]:
            if deja_visite[k] == 0:
                compteur[noeud] = 0

                for j in noeuds_visites:
                    compteur[j] += 1

                explore(k)

                branche_plus_longue[k] = max(branche_plus_longue[k], n - compteur[j])
                minimum = min(minimum, branche_plus_longue[k])
                maxi = max(compteur[noeud], maxi)

        branche_plus_longue[noeud] = maxi
        noeuds_visites.pop()

    ## Programme
    # explore(0)

    pile = deque([0])

    while pile:
        noeud = pile.pop()
        print("\n\nnoeud", noeud)
        print("-----------")
        deja_visite[noeud] = 1
        noeuds_visites.append(noeud)

        maxi = branche_plus_longue[noeud]

        for k in sortant[noeud]:
            if deja_visite[k] == 0:
                compteur[noeud] = 0
                pile.append(k)

                for j in noeuds_visites:
                    compteur[j] += 1

                print("noeuds_visites", noeuds_visites)

                branche_plus_longue[k] = max(branche_plus_longue[k], n - compteur[j])
                minimum = min(minimum, branche_plus_longue[k])
                maxi = max(compteur[noeud], maxi)
            else:
                noeuds_visites.pop()

        branche_plus_longue[noeud] = maxi
        # noeuds_visites.pop()

    print(minimum)
    print(branche_plus_longue)

    # todo 1) rajouter l'optimisation pour les feuilles, et les noeuds avec 2 arêtes
    # todo 2) coder en itératif plutôt que récursif
    # todo 3) pour le "compteur[j] += 1", plutôt que d'incrémenter de 1 en 1,
    # todo       > tout incrémenter d'un coup !!!

    # todo bug) la 1ère case "branche_plus_longue" vaut 18 pour l'exemple de test ????
    # todo => à cause de l'opti du todo 1


main()
