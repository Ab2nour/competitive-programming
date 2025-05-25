L, C = map(int, input().split())

labyrinthe = [list(input()) for i in range(L)]

compteur = 0


def parcours(labyrinthe, x, y):  # coordonnées x et y de la case
    global compteur

    # if case >= 0 and case < len(labyrinthe): # on vérifie qu'on est pas sorti
    if x >= 0 and x < L and y >= 0 and y < C:  # on vérifie qu'on est pas sorti
        if labyrinthe[x][y] == True or labyrinthe[x][y] == "#":
            return 0

        if labyrinthe[x][y] == ".":
            compteur += 1
            labyrinthe[x][y] = True
            # appels récursifs sur les cases d'à côté
            parcours(labyrinthe, x, y + 1)  # droite
            parcours(labyrinthe, x, y - 1)  # gauche
            parcours(labyrinthe, x - 1, y)  # haut
            parcours(labyrinthe, x + 1, y)  # bas


nb_cases = L * C
nb_zones = 0

for i in range(L):
    for j in range(C):
        if labyrinthe[i][j] == ".":  # calcul du nombre de #
            nb_zones += 1
            parcours(labyrinthe, i, j)

print(nb_zones)
