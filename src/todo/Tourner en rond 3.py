def main():
    import sys
    sys.setrecursionlimit(10**9)

    N, A = map(int, input().split())

    class Noeud:
        def __init__(self, nom):
            self.nom = nom

    graphe = [Noeud(i) for i in range(N+1)]

    for i in range(N+1):
        graphe[i].sortant = []
        graphe[i].deja_visite = "blanc"

    for i in range(A):
        a, b = map(int, sys.stdin.readline().split())
        graphe[a].sortant.append(graphe[b])

    def visite(noeud):
        if noeud.deja_visite == "gris":
            print("OUI")
            exit()

        elif len(noeud.sortant) > 0 and noeud.deja_visite == "blanc":
            noeud.deja_visite = "gris"
            for i in noeud.sortant:
                visite(i)
            noeud.deja_visite = "noir"


    visite(graphe[1])
    print("NON")

main()