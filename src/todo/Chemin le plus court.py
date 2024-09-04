import sys
sys.setrecursionlimit(10**9)

L, C = map(int, input().split())

labyrinthe = [list(input()) for i in range(L)]

file = []
chemin = []

def check_case(x, y, n):
    """ Teste si la case [x][y] du labyrinthe vaut le coup d'être testée.
        La case doit être plus proche de la sortie, elle doit contenir une valeur
        inférieure à n."""
    if 0 <= x < L and 0 <= y < C:
        if isinstance(labyrinthe[x][y], int): # la case contient un entier
            if labyrinthe[x][y] < n:
                return True

def visite(x, y):
    """ Parcours en profondeur récursif pour trouver le chemin idéal. """
    global L, C, labyrinthe, chemin

    n = labyrinthe[x][y]

    if x == L-1 and y == C-2:
        for i in chemin:
            print(i, end="")
        exit()

    if check_case(x, y+1, n):
        chemin.append("E")
        visite(x, y+1)
        chemin.pop()
    if check_case(x-1, y, n):
        chemin.append("N")
        visite(x-1, y)
        chemin.pop()
    if check_case(x, y-1, n):
        chemin.append("O")
        visite(x, y-1)
        chemin.pop()
    if check_case(x+1, y, n):
        chemin.append("S")
        visite(x+1, y)
        chemin.pop()

def marque_distance(x, y, n):
    """ Parcours en largeur pour marquer la distance n des cases de la sortie.
        Renvoie True dès qu'on est sur la case d'entrée (job fini). """
    global L, C, labyrinthe, file

    if 0 <= x < L and 0 <= y < C:
        if x == 1 and y == 0:
            labyrinthe[x][y] = n
            return True

        if labyrinthe[x][y] == ".":
            labyrinthe[x][y] = n
            file.append((x, y, n))

    return False

file.append((L-1, C-2, 0)) # on remplit la file avec la sortie du labyrinthe
labyrinthe[L-1][C-2] = 0

while file:
    noeud = file.pop(0)
    x, y, n = noeud # équivalent à x = noeud[0] et y = noeud[1] et n = noeud[2]

    if marque_distance(x, y+1, n+1):
        break
    if marque_distance(x-1, y, n+1):
        break
    if marque_distance(x, y-1, n+1):
        break
    if marque_distance(x+1, y, n+1):
        break

print(labyrinthe[1][0]) # distance du plus court chemin
visite(1, 0)