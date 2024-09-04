entree = """12 5
1 3 2 2 5 4 3 2 5 5 1 4"""

entree = entree.split("\n")

index = 0
def readline():
    global index, entree
    index += 1
    return entree[index-1]

import sys
sys.stdin.readline = readline
input = readline

### copier en-dessous
import sys
readline = sys.stdin.readline


## Traitement données
nb_jours, nb_groupes = map(int, readline().split())
festival = list(map(int, readline().split()))


## Variables
groupes_presents = [-1 for i in range(nb_groupes+1)]
groupes_presents[0] = 0 # la case 0 est un compteur du nombre de groupes présents
    # la case i indique si le groupe i est présent
intervalle_max = nb_jours
    # pas besoin de tester un intervalle plus grand que le max qu'on a trouvé

i = 0
intervalle_actif = 0


## Programme
while i + intervalle_actif < nb_jours: # parcours de chaque case de festival
    print("--------------------")
    print("je pars de la case i =", i)
    while intervalle_actif < intervalle_max and i + intervalle_actif < nb_jours:
        print(festival[i + intervalle_actif])
        #print(groupes_presents)
        if groupes_presents[festival[i + intervalle_actif]] < i:
            groupes_presents[0] += 1
            groupes_presents[festival[i + intervalle_actif]] = i

            if groupes_presents[0] == nb_groupes:
                print("roger")
                print("intervalle_actif", intervalle_actif)
                intervalle_max = intervalle_actif
                break

        intervalle_actif += 1

    i += 1
    groupes_presents[0] = 0

    if i + intervalle_actif <= nb_jours and intervalle_actif <= nb_groupes:
        intervalle_actif = 0 # ou 1 ?
    else: # on s'arrête si on a trouvé le max possible ou que ça sera impossible
        break


## Affichage réponse
print(intervalle_max+1)