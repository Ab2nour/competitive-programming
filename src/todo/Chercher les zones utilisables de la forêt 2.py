import sys
sys.setrecursionlimit(10**9)

N, A = map(int, input().split())
zones = 0
intersections = [0 for i in range(N)] # nb d'intersections pour chaque zone (max N zones)

class Noeud:
    def __init__(self, nom):
        self.nom = nom

graphe = [Noeud(i) for i in range(N+1)]

for i in range(N+1):
    graphe[i].entrant = []
    graphe[i].sortant = []
    graphe[i].deja_visite = False

for i in range(A):
    a, b, non_utilise = map(int, input().split())
    graphe[a].sortant.append(graphe[b])
    graphe[b].entrant.append(graphe[a])


def visite(noeud):
    if noeud.deja_visite == False:
        noeud.deja_visite = True
        intersections[zones] += 1
        if len(noeud.sortant) > 0:
            for i in noeud.sortant:
                visite(i)
        if len(noeud.entrant) > 0:
            for i in noeud.entrant:
                visite(i)
        return True

    else:
        return False


for i in range(1, N):
    if visite(graphe[i]):
        zones += 1

print(zones, max(intersections))