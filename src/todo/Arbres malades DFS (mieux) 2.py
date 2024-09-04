def main():
    import sys
    from array import array
    from collections import deque

    sys.setrecursionlimit(10**8)


    ### Variables
    n, m = map(int, input().split())

    arbres = [[] for i in range(n)] # noeud
    arbres_a_cote = [deque(maxlen=200) for i in range(n)] # arêtes

    deja_visite = [False for i in range(n)]

    nb_arbres_contamines = array("i", [-1 for i in range(n)]) # on stocke les résultats
                                    # si on demande plusieurs fois le même arbre


    ### Fonctions
    def distance(x1, y1, x2, y2):
        return (x2-x1)**2 + (y2-y1)**2

    def explore(noeud):
        nonlocal compteur, deja_visite # variables globales, à l'intérieur du main()

        deja_visite[noeud] = True
        compteur += 1

        liste_a_rajouter = deque(maxlen=200)

        if nb_arbres_contamines[noeud] == 200:
            compteur = 200
            deja_visite = [True for i in range(n)]
            break

        else:
            for k in range(len(arbres_a_cote[noeud])): # pour chaque voisin du noeud
                if nb_arbres_contamines[noeud] == 200: # à déplacer car n'a rien à voir
                                                        # avec le for
                    compteur = 200
                    deja_visite = [True for i in range(n)]
                    break

                # mettre le arbres_a_cote[noeud][k]] dans une variable
                #   > pour simplifier l'écriture
                    break
                elif not deja_visite[arbres_a_cote[noeud][k]]:
                    liste_a_rajouter.append(arbres_a_cote[noeud][k])
                    explore(arbres_a_cote[noeud][k])



    ### Traitement des données
    for i in range(n):
        x, y, r = map(int, sys.stdin.readline().split())
        arbres[i] = (x, y, r**2)

    # Création du graphe
    for i in range(n):
        x1, y1, r = arbres[i]

        for j in range(n):
            x2, y2, _ = arbres[j] # "_" est ignoré
            if i != j and distance(x1, y1, x2, y2) <= r:
                arbres_a_cote[i].append(j)


    ### Programme
    for i in range(m):
        compteur = 0
        arbre_a_test = int(sys.stdin.readline())

        if nb_arbres_contamines[arbre_a_test] == -1:
            explore(arbre_a_test)
            deja_visite = [False for i in range(n)]

            nb_arbres_contamines[arbre_a_test] = compteur

        sys.stdout.write("%s\n" %(nb_arbres_contamines[arbre_a_test]))

main()