import sys

sys.setrecursionlimit(10**8)

N, K = map(int, input().split())

chemin = []


def parcours(noeud, nb_restant):
    global chemin
    if nb_restant > 0:
        chemin.append(noeud)
        for i in range(noeud, N + 1):
            parcours(i, nb_restant - 1)
        chemin.pop()
    else:
        chemin.append(noeud)
        for i in chemin:
            sys.stdout.write("%s " % i)
        sys.stdout.write("\n")

        chemin.pop()


for i in range(1, N + 1):
    parcours(i, K - 1)
