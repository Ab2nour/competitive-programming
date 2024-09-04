import sys
from array import array
sys.setrecursionlimit(10**9)

L, C = map(int, input().split())

#labyrinthe = tuple([list(input()) for i in range(L)])
labyrinthe = []
for i in range(L):
    nouvelle_ligne = list(input())
    for j in range(C):
        if nouvelle_ligne[j] == "#":
            nouvelle_ligne[j] = 10**6+1
        else:
            nouvelle_ligne[j] = -1
    labyrinthe.append(array("i", nouvelle_ligne))
del nouvelle_ligne


file = []

def check_case(x, y, n):
    """ Teste si la case [x][y] du labyrinthe vaut le coup d'être testée.
        La case doit être plus proche de la sortie, elle doit contenir une valeur
        inférieure à n."""
    if 0 <= x < L and 0 <= y < C:
        if isinstance(labyrinthe[x][y], int): # la case contient un entier
            if 0 <= labyrinthe[x][y] < n:
                return True

def visite(x, y):
    """ Parcours pour trouver le chemin idéal. """
    global L, C, labyrinthe

    n = labyrinthe[x][y]

    for i in range(labyrinthe[1][0]):
        if check_case(x, y+1, n):
            sys.stdout.write("E")
            x, y, n = x, y+1, n-1
        elif check_case(x-1, y, n):
            sys.stdout.write("N")
            x, y, n = x-1, y, n-1
        elif check_case(x, y-1, n):
            sys.stdout.write("O")
            x, y, n = x, y-1, n-1
        elif check_case(x+1, y, n):
            sys.stdout.write("S")
            x, y, n = x+1, y, n-1


def marque_distance(x, y, n):
    """ Parcours en largeur pour marquer la distance n des cases de la sortie.
        Renvoie True dès qu'on est sur la case d'entrée (job fini). """
    global L, C, labyrinthe, file

    if 0 <= x < L and 0 <= y < C:
        if x == 1 and y == 0:
            labyrinthe[x][y] = n
            return True

        if labyrinthe[x][y] == -1:
            labyrinthe[x][y] = n
            file.append(x)
            file.append(y)

    return False

file.append(L-1)
file.append(C-2) # on remplit la file avec la sortie du labyrinthe
labyrinthe[L-1][C-2] = 0

while file:
    x = file.pop(0)
    y = file.pop(0)
    n = labyrinthe[x][y]

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