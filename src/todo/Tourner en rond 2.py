import sys

sys.setrecursionlimit(10**9)

N, A = map(int, input().split())


class Noeud:
    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return str(self.nom)


graphe = [Noeud(i) for i in range(N + 1)]

for i in range(N + 1):
    graphe[i].sortant = []
    graphe[i].deja_visite = False

for i in range(A):
    a, b = map(int, input().split())
    graphe[a].sortant.append(graphe[b])

pile = [graphe[1]]
graphe[1].deja_visite = True

while pile:
    noeud_en_cours = pile.pop()
    for noeud in noeud_en_cours.sortant:
        if noeud.deja_visite == False:
            noeud.deja_visite = True
            pile.append(noeud)
        else:
            print("OUI")
            exit()

print("NON")
