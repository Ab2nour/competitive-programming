L, C = map(int, input().split())

labyrinthe = [list(input()) for i in range(L)]

compteur = 0
deja_visite =  [[False for i in range(C)] for i in range(L)]

def parcours(labyrinthe, x, y): # coordonnées x et y de la case
    global compteur

    #if case >= 0 and case < len(labyrinthe): # on vérifie qu'on est pas sorti
    if x >= 0 and x < L and y >= 0 and y < C: # on vérifie qu'on est pas sorti
        if deja_visite[x][y] == True:
            return 0
        else:
            deja_visite[x][y] = True

        if x == L-1 and y == C-2: # la sortie !
            compteur += 1

        if labyrinthe[x][y] == '.':
            # appels récursifs sur les cases d'à côté
            parcours(labyrinthe, x, y+1) # droite
            parcours(labyrinthe, x, y-1) # gauche
            parcours(labyrinthe, x-1, y) # haut
            parcours(labyrinthe, x+1, y) # bas

        deja_visite[x][y] = False


parcours(labyrinthe, 1, 0)

print(compteur)