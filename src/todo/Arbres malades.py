import sys
sys.setrecursionlimit(10**8)


### Variables
n, m = map(int, input().split())

arbres = [[] for i in range(n)]
arbres_a_cote = [[] for i in range(n)]
deja_visite = [False for i in range(n)]


### Fonctions
def distance(x1, y1, x2, y2):
    return (x2-x1)**2 + (y2-y1)**2

def explore(noeud):
    global compteur

    deja_visite[noeud] = True
    compteur += 1

    for k in range(len(arbres_a_cote[noeud])):
        if not deja_visite[arbres_a_cote[noeud][k]]:
            explore(arbres_a_cote[noeud][k])
    #deja_visite[noeud] = False


### Traitement des données
for i in range(n):
    x, y, r = map(int, sys.stdin.readline().split())
    arbres[i] = (x, y, r**2)

for i in range(n):
    x1, y1, r = arbres[i]
    for j in range(n):
        x2, y2, _ = arbres[j] # "_" est ignoré
        if distance(x1, y1, x2, y2) <= r:
            arbres_a_cote[i].append(j)


### Programme
for i in range(m):
    compteur = 0

    arbre_a_test = int(sys.stdin.readline())
    explore(arbre_a_test)
    deja_visite = [False for i in range(n)]
    print(compteur)
