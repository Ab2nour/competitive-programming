import sys

sys.setrecursionlimit(10**8)


class Noeud:
    def __init__(self, nom, pere=None, fils=None):
        self.nom = nom
        self.pere = pere
        if fils == None:
            self.fils = []
        else:
            self.fils = fils

    def __repr__(self):
        return "Noeud " + self.nom

    def to_the_top(self):
        compteur = 0
        noeud_actuel = self
        while noeud_actuel != None:
            noeud_actuel = noeud_actuel.pere
            compteur += 1
        return compteur


def to_the_top(noeud):
    return noeud.to_the_top()


N = int(input())
liste_pour_noeuds = list(map(int, "3 3 7 3 6 7 0 0".split()))
liste_pour_noeuds = list(map(int, input().split()))

noeuds = [0 for i in range(N)]

for i in range(N):
    noeuds[i] = Noeud(str(i + 1))

for i in range(N):
    indice = liste_pour_noeuds[i] - 1
    if indice > 0:
        noeuds[i].pere = noeuds[indice]
        noeuds[i].pere.fils.append(noeuds[i])

max = 0

for i in range(N):
    if not noeuds[i].fils:  # noeuds[i] n'a pas de fils
        a = noeuds[i].to_the_top()
        if a > max:
            max = a
print(max)
# 3 3 7 3 6 7 0 0
