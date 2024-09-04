import sys


## ---------- Données ----------
from array import array


MAX_ZOINXIEN = 200000

deja_vu_x = array("b", [0 for i in range(MAX_ZOINXIEN+1)])
deja_vu_y = array("b", [0 for i in range(MAX_ZOINXIEN+1)])
deja_vu_tentacule = array("b", [0 for i in range(MAX_ZOINXIEN+1)])
deja_vu_age = array("b", [0 for i in range(MAX_ZOINXIEN+1)])

deja_vu = array("b", [0 for i in range(MAX_ZOINXIEN+1)])

zoinxiens = [0 for i in range(MAX_ZOINXIEN)]


# liste des zoinxiens qui vérifient telle propriété
# exemple : propriete_age[5] est une liste qui contient tous les
#   > zoinxiens qui ont 5 ans

propriete_x = [[] for i in range(MAX_ZOINXIEN+1)]
propriete_y = [[] for i in range(MAX_ZOINXIEN+1)]
propriete_age = [[] for i in range(MAX_ZOINXIEN+1)]
propriete_tentacule = [[] for i in range(MAX_ZOINXIEN+1)]


## ---------- Fonctions ----------
def marque_age(n):
    """ Fonction pour marquer les cases adjacentes à l'âge (plus ou moins 5 ans). """
    if n < 5:
        for i in range(0, (n + 1) + 5):
            deja_vu_age[i] = 1

    elif n > MAX_ZOINXIEN - 5:
        for i in range(n-5, MAX_ZOINXIEN + 1):
            deja_vu_age[i] = 1

    else:
        for i in range(n-5, (n + 1) + 5):
            deja_vu_age[i] = 1

def marque_propriete_age(age, id_zox):
    """ Idem que marque_age mais pour les propriétés. """
    if age < 5:
        for i in range(0, (age + 1) + 5):
            propriete_age[i].append(id_zox)

    elif age > MAX_ZOINXIEN - 5:
        for i in range(age-5, MAX_ZOINXIEN + 1):
            propriete_age[i].append(id_zox)

    else:
        for i in range(age-5, (age + 1) + 5):
            propriete_age[i].append(id_zox)

def deja_vu_zoinxien(id_zox):
    """ Fonction pour marquer tous les attributs d'un Zoinxien comme déjà vus. """
    x = zoinxiens[id_zox][0]
    y = zoinxiens[id_zox][1]
    tentacule = zoinxiens[id_zox][2]
    age = zoinxiens[id_zox][3]

    deja_vu_x[x] = 1
    deja_vu_y[y] = 1
    deja_vu_tentacule[tentacule] = 1
    marque_age(age)
    deja_vu[id_zox] = 1

def est_ami(id_zox):
    """ Fonction pour savoir si un Zoinxien est ami, selon les données actuelles. """
    x = zoinxiens[id_zox][0]
    y = zoinxiens[id_zox][1]
    tentacule = zoinxiens[id_zox][2]
    age = zoinxiens[id_zox][3]

    if deja_vu_x[x] or deja_vu_y[y] or deja_vu_tentacule[tentacule] or deja_vu_age[age]:
        return True
    else:
        return False

def rajoute_amis(id_zox):
    """ Rajoute les amis d'un zoinxien à la pile de parcours. """
    x = zoinxiens[id_zox][0]
    y = zoinxiens[id_zox][1]
    tentacule = zoinxiens[id_zox][2]
    age = zoinxiens[id_zox][3]

    if not deja_vu_x[x]:
        for i in propriete_x:
            if not deja_vu[i]:
                pile.append(i)

    if not deja_vu_y[y]:
        for i in propriete_y:
            if not deja_vu[i]:
                pile.append(i)

    if not deja_vu_tentacule[tentacule]:
        for i in propriete_tentacule:
            if not deja_vu[i]:
                pile.append(i)

    if not deja_vu_age[age]:
        for i in propriete_age:
            if not deja_vu[age]:
                pile.append(i)


## ---------- Entrées ----------
n = int(input())

for i in range(n):
    zoinxiens[i] = array("i", (map(int, sys.stdin.readline().split())))

    propriete_x[zoinxiens[i][0]].append(i)
    propriete_y[zoinxiens[i][1]].append(i)
    propriete_tentacule[zoinxiens[i][2]].append(i)
    marque_propriete_age(zoinxiens[i][3], i)


## ---------- Code ----------
deja_vu_zoinxien(0)
nb_amis = 0

pile = [0]

while pile:
    id_zox = pile.pop()

    x = zoinxiens[id_zox][0]
    y = zoinxiens[id_zox][1]
    tentacule = zoinxiens[id_zox][2]
    age = zoinxiens[id_zox][3]

    if est_ami(id_zox):
        rajoute_amis(id_zox)
        deja_vu_zoinxien(id_zox)
        nb_amis += 1


print(nb_amis)

