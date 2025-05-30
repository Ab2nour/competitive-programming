import sys
from collections import deque

write = sys.stdout.write


## Fonctions
def decompose_nombre(n):
    """Décompose en nombre en un tableau qui représente ses chiffres
    Ex : 123 devient [1, 2, 3]
    """
    puissance_dix = 1

    while 10**puissance_dix <= n:
        puissance_dix += 1

    tab = [0 for i in range(puissance_dix)]

    for i in range(1, puissance_dix + 1):
        tab[-i] = n % 10
        n = (n - n % 10) // 10

    return tab


def verif_masque(masque, nombre):
    n = decompose_nombre(nombre)

    if nombre == 0 or len(n) != len(masque):
        return False

    else:
        for i in range(len(n)):
            if masque[i] != -1:
                if masque[i] != n[i]:
                    return False

    return True


## Classe
class Noeud:
    def __init__(self, nom, fils=None):
        self.nom = nom

        if fils == None:
            self.fils = []

    def __repr__(self):
        # return "Noeud " + self.nom
        return str(self.nom)


## Entrées
N = int(input())
liste_pour_noeuds = list(map(int, sys.stdin.readline().split()))

masque = input()
masque = [int(i) if (i != "?") else -1 for i in masque]
# chaque "?" devient un -1, les nombres restent inchangés
# ex : masque = "12?3?" devient [1, 2, -1, 3, -1]


## Création de l'arbre à partir des données
noeuds = tuple([Noeud(i) for i in range(N + 1)])  # todo remettre en liste ?

for i in range(1, N + 1):
    indice = liste_pour_noeuds[i - 1]
    noeuds[indice].fils.append(noeuds[i])


## Breadth-First Search
file = deque([noeuds[0]])

while file:
    noeud = file.popleft()

    if verif_masque(masque, noeud.nom):
        write("%d " % noeud.nom)

    for i in noeud.fils:
        file.append(i)


# todo remplace la classe noeuds par un tableau de fils "sortant"
