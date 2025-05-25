L, C = map(int, input().split())

labyrinthe = [list(input()) for i in range(L)]

deja_visite = [[False for i in range(C)] for j in range(L)]

N = int(input())

compteur = [0 for i in range(N + 1)]

file = []


def visite(x, y, n):
    global N, compteur, file

    if 0 <= x < L and 0 <= y < C:
        if n >= N:
            return False
        if deja_visite[x][y] == False and labyrinthe[x][y] == ".":
            deja_visite[x][y] = True
            file.append((x, y, distance + 1))
            compteur[distance + 1] += 1

    return True


file.append((L - 1, C - 2, 0))
deja_visite[L - 1][C - 2] = True

while file:
    # print(file)
    noeud = file.pop(0)
    x, y, distance = (
        noeud  # équivalent à x = noeud[0] et y = noeud[1] et distance = noeud[2]
    )

    if not visite(x + 1, y, distance):
        break
    if not visite(x - 1, y, distance):
        break
    if not visite(x, y + 1, distance):
        break
    if not visite(x, y - 1, distance):
        break

for i in range(1, N + 1):
    print(compteur[i], end=" ")
