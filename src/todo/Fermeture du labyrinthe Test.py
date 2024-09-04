entree = """12 16
1 2
1 3
2 4
2 6
3 6
3 7
4 5
5 7
5 9
5 10
6 5
7 8
8 11
9 12
10 9
11 10"""

entree = entree.split("\n")

index = 0
def readline():
    global index, entree
    index += 1
    return entree[index-1]

from array import array
import sys
N, A = map(int, readline().split())
sortant = [[] for i in range(N+1)]
nb_noeuds_entrants = [0 for i in range(N+1)]

rien_a_afficher = False

for i in range(A):
    a, b = map(int, readline().split())
    sortant[a].append(b)
    nb_noeuds_entrants[b] += 1

### copier le code en-dessous

### Fonctions
def aucun_ancetre(noeud):
    if nb_noeuds_entrants[noeud] > 0:
            return False
    return True

def supprime_fils(noeud):
    if len(sortant[noeud]) > 0:
        liste_fils_a_visiter = []

        for i in range(1, len(sortant[noeud])+1):
            nb_noeuds_entrants[sortant[noeud][i-1]] -= 1
            if aucun_ancetre(sortant[noeud][i-1]): # si c'était le dernier lien, on le stocke
                ordre.append(sortant[noeud][i-1]) # et on le rajoute à l'ordre de parcours
                liste_fils_a_visiter.append(sortant[noeud][i-1])

        for i in liste_fils_a_visiter:
            supprime_fils(i)

### Variables
rien_a_afficher = False
liste_sans_ancetre = []
ordre = []


### On repère tous les noeuds qui n'ont pas d'ancêtre
for i in range(1, N+1):
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
        sys.stdout.write("%s " %ordre[i])