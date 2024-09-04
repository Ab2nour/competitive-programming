n, a = map(int, input().split())

noeuds = [i for i in range(n+1)]
entrant = [[] for i in range(n+1)]
sortant = [[] for i in range(n+1)]
indispensable = [[] for i in range(n+1)]

profondeur = [0 for i in range(n+1)]
noeuds_en_visite = []


for i in range(a):
    n1, n2 = map(int, input().split())

    # pour le parcours on regarde les noeuds sortant
    # pour les arêtes indispensables on
    # regarde les noeuds entrants
    sortant[n1].append(n2)
    sortant[n2].append(n1)
    entrant[n2].append(n1)

    indispensable[n2].append(True)


def parcours(noeud, p):
    if profondeur[noeud] > 0: # déjà visité
        for i in noeuds_en_visite:
            if profondeur[i] > p:
                for j in range(len(entrant[i])):
                    entrant[j] = False
    else:
        profondeur[noeud] = p
        noeuds_en_visite.append(noeud)

        for i in sortant[noeud]:
            parcours(i, p+1)

        profondeur[noeud] = 0
        noeuds_en_visite.pop()


