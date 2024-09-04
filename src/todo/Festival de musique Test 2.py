entree = """22 5
1 1 1 1 1 1 1 1 1 1 1 3 2 2 5 4 3 2 5 5 1 4"""

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
def main():
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
    somme_i_ia = i + intervalle_actif


    ## Programme
    while somme_i_ia < nb_jours: # parcours de chaque case de festival
        while intervalle_actif < intervalle_max and somme_i_ia < nb_jours and festival[i] != festival[i+1]:
            # si la case d'après est identique, on la passe

            if groupes_presents[festival[somme_i_ia]] < i:
                groupes_presents[0] += 1
                groupes_presents[festival[somme_i_ia]] = i

                if groupes_presents[0] == nb_groupes:
                    intervalle_max = intervalle_actif
                    break

            intervalle_actif += 1
            somme_i_ia = i + intervalle_actif

        i += 1
        groupes_presents[0] = 0

        if i + intervalle_actif <= nb_jours and intervalle_max >= nb_groupes:
            intervalle_actif = 0 # ou 1 ?
            somme_i_ia = i
        else: # on s'arrête si on a trouvé le max possible ou que ça sera impossible
            break


    ## Affichage réponse
    print(intervalle_max+1)

main()