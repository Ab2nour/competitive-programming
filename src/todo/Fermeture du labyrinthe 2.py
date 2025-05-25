import sys

sys.setrecursionlimit(10**8)


### Fonctions
def aucun_ancetre(noeud):
    if nb_noeuds_entrants[noeud] > 0:
        return False
    return True


def supprime_fils(noeud):
    if len(sortant[noeud]) > 0:
        liste_fils_a_visiter = []

        for i in range(1, len(sortant[noeud]) + 1):
            nb_noeuds_entrants[sortant[noeud][i - 1]] -= 1
            if aucun_ancetre(
                sortant[noeud][i - 1]
            ):  # si c'était le dernier lien, on le stocke
                ordre.append(
                    sortant[noeud][i - 1]
                )  # et on le rajoute à l'ordre de parcours
                liste_fils_a_visiter.append(sortant[noeud][i - 1])

        for i in liste_fils_a_visiter:
            supprime_fils(i)


### Traitement des données
N, A = map(int, sys.stdin.readline().split())
# entrant = [[] for i in range(N+1)]
sortant = [[] for i in range(N + 1)]
nb_noeuds_entrants = [0 for i in range(N + 1)]

for i in range(A):
    a, b = map(int, sys.stdin.readline().split())
    sortant[a].append(b)
    nb_noeuds_entrants[b] += 1


### Variables
rien_a_afficher = False
liste_sans_ancetre = []
ordre = []


### On repère tous les noeuds qui n'ont pas d'ancêtre
for i in range(1, N + 1):
    if aucun_ancetre(i):
        liste_sans_ancetre.append(i)


### On parcourt tous ces noeuds sans ancêtre, s'il y en a
if len(liste_sans_ancetre) == 0:
    rien_a_afficher = True
else:
    for i in liste_sans_ancetre:
        ordre.append(i)
        supprime_fils(i)


### Affichage des résultats, dans l'ordre de la liste "ordre"
if rien_a_afficher or len(ordre) < N:
    print(-1)
else:
    for i in range(len(ordre)):
        sys.stdout.write("%s " % ordre[i])
