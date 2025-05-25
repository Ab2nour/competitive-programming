L, C = map(int, input().split())

labyrinthe = [list(input()) for i in range(L)]

compteur = 0
deja_visite = [[False for i in range(C)] for i in range(L)]


def parcours(labyrinthe, x, y):  # coordonnées x et y de la case
    global compteur

    # if case >= 0 and case < len(labyrinthe): # on vérifie qu'on est pas sorti
    if x >= 0 and x < L and y >= 0 and y < C:  # on vérifie qu'on est pas sorti
        if deja_visite[x][y] == True:
            return 0
        else:
            deja_visite[x][y] = True

        if labyrinthe[x][y] == ".":
            compteur += 1
            # appels récursifs sur les cases d'à côté
            parcours(labyrinthe, x, y + 1)  # droite
            parcours(labyrinthe, x, y - 1)  # gauche
            parcours(labyrinthe, x - 1, y)  # haut
            parcours(labyrinthe, x + 1, y)  # bas


parcours(labyrinthe, 1, 0)

nb_cases = L * C
nb_dieses = 0

for i in range(L):
    for j in range(C):
        if labyrinthe[i][j] == "#":  # calcul du nombre de #
            nb_dieses += 1

print(L * C - compteur - nb_dieses)
