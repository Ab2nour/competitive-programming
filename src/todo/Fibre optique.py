def main():
    import sys

    sys.setrecursionlimit(10**8)
    readline = sys.stdin.readline

    ## Variables
    n = int(input())

    sortant = [[] for i in range(n)]
    taille_branche_plus_longue = [0 for i in range(n)]
    deja_visite = [0 for i in range(n)]
    BLANC, GRIS, NOIR = 0, 1, 2  # 0, 1, 2 => blanc, gris, noir

    ## Construction de l'arbre
    for i in range(n - 1):
        a, b = map(int, readline().split())
        sortant[a].append(b)
        sortant[b].append(a)

    ## Fonctions
    def explore(noeud, couleur=0):
        nonlocal compteur

        compteur += 1
        deja_visite[noeud] = GRIS

        for k in sortant[noeud]:
            if deja_visite[k] == BLANC or deja_visite[k] == NOIR:
                explore(k, deja_visite[k])

        deja_visite[noeud] = couleur

    ## Programme
    for i in range(n):
        maxi = taille_branche_plus_longue[i]
        deja_visite[i] = GRIS

        for j in sortant[i]:
            compteur = 0

            if len(sortant[i]) == 1:
                maxi = n - 1  # pas besoin de parcourir si le noeud est une feuille
                taille_branche_plus_longue[j] = max(1, taille_branche_plus_longue[j])

            elif deja_visite[j] == BLANC:
                explore(j)
                maxi = max(compteur, maxi)
                taille_branche_plus_longue[j] = max(
                    n - compteur, taille_branche_plus_longue[j]
                )

        deja_visite[i] = NOIR

        taille_branche_plus_longue[i] = maxi

    print(min(taille_branche_plus_longue))


main()
