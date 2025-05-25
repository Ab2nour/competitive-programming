import sys

sys.setrecursionlimit(10**8)


class Noeud:
    def __init__(self, nom, pere=None, fils=None):
        self.nom = nom
        self.pere = pere
        self.fils = fils

    def __repr__(self):
        return "Noeud " + self.nom

    def to_the_top(self):
        noeud_actuel = self
        while noeud_actuel != None:
            # print(noeud_actuel)
            print(noeud_actuel.nom, end=" ")
            noeud_actuel = noeud_actuel.pere
        print("")

    def to_the_top(self):
        noeud_actuel = self
        if noeud_actuel.pere == None:
            print(noeud_actuel.nom, end=" ")
            return 0
        else:
            to_the_top(noeud_actuel.pere)
            print(noeud_actuel.nom, end=" ")


class Arbre:
    def __init__(self, racine):
        self.racine = racine

    def __repr__(self):
        return "Arbre de racine " + self.racine.nom


def to_the_top(noeud):
    noeud.to_the_top()


# A
# B | C
# D E F | G H
A = Noeud("A")
B = Noeud("B", A)
C = Noeud("C", A)
D = Noeud("D", B)
E = Noeud("E", B)
F = Noeud("F", B)
G = Noeud("G", C)
H = Noeud("H", C)

A.fils = [B, C]
B.fils = [D, E, F]
C.fils = [G, H]


ar = Arbre(A)

N = int(input())
liste_pour_noeuds = list(map(int, input().split()))
R = int(input())
liste_requetes = list(map(int, input().split()))

noeuds = [0 for i in range(N)]
for i in range(N):
    noeuds[i] = Noeud(str(i + 1))
for i in range(N):
    indice = liste_pour_noeuds[i] - 1
    if indice > 0:
        noeuds[i].pere = noeuds[indice]


def affiche_chemin(index):
    to_the_top(noeuds[index - 1])
    print()


for i in range(R):
    affiche_chemin(liste_requetes[i])

# exemple de bug :
# 5
# 4 1 2 0 0
# 3
# 1
# peut-être que c'est quand une des cases du tableau vaut 1
