import sys

readline = sys.stdin.readline


## Traitement données
nb_jours, nb_groupes = map(int, readline().split())
festival = list(map(int, readline().split()))


## Variables
groupes_presents = [0 for i in range(nb_groupes)]
# la case 0 est un compteur du nombre de groupes présents
# la case i indique si le groupe i est présent
intervalle_max = nb_jours
# pas besoin de tester un intervalle plus grand que le max qu'on a trouvé

i = 0
intervalle_actif = 0


## Programme
while i + intervalle_actif < nb_jours:  # parcours de chaque case de festival
    while intervalle_actif < intervalle_max and i + intervalle_actif < nb_jours:
        if groupes_presents[festival[i]] == 0:
            groupes_presents[0] += 1
            groupes_presents[festival[i]] = 1

        if groupes_presents[0] == nb_groupes:
            intervalle_max = intervalle_actif
            intervalle_actif = 0  # ou 1 ?
            break

        intervalle_actif += 1

    i += 1
    groupes_presents = [0 for i in range(nb_groupes)]


## Affichage réponse
print(intervalle_max)
