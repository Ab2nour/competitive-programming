import sys

sys.setrecursionlimit(10**9)

N, A = map(int, input().split())
zones = 0
intersections = [
    1 for i in range(N)
]  # nb d'intersections pour chaque zone (max N zones)

graphe = [[] for i in range(N + 1)]
deja_visite = [False for i in range(N + 1)]

for i in range(A):
    a, b, non_utilise = map(int, input().split())
    graphe[a].append(b)


def visite(noeud):
    if len(graphe[noeud]) > 0 and deja_visite[noeud] == False:
        deja_visite[noeud] = True
        intersections[zones] += 1
        for i in graphe[noeud]:
            visite(i)

        return True

    else:
        return False


for i in range(1, N):
    if visite(i):
        zones += 1

print(zones, max(intersections))
