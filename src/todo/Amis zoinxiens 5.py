import sys


## ---------- Données ----------
from array import array
from collections import deque


MAX_ZOINXIEN = 200000

deja_vu_x = [[0] for i in range(MAX_ZOINXIEN+1)]
deja_vu_y = [[0] for i in range(MAX_ZOINXIEN+1)]
deja_vu_tentacule = [[0] for i in range(MAX_ZOINXIEN+1)]
deja_vu_age = [[0] for i in range(MAX_ZOINXIEN+1)]

deja_vu = array("b", [0 for i in range(MAX_ZOINXIEN+1)])

zoinxiens = [0 for i in range(MAX_ZOINXIEN)]


## ---------- Fonctions ----------
def marque_age(age, id_zox):
    """ Idem que marque_age mais pour les propriétés. """
    if age < 5:
        for i in range(0, (age + 1) + 5):
            deja_vu_age[i].append(id_zox)
            deja_vu_age[i][0] = 1

    elif age > MAX_ZOINXIEN - 5:
        for i in range(age-5, MAX_ZOINXIEN + 1):
            deja_vu_age[i].append(id_zox)
            deja_vu_age[i][0] = 1

    else:
        for i in range(age-5, (age + 1) + 5):
            deja_vu_age[i].append(id_zox)
            deja_vu_age[i][0] = 1

def deja_vu_zoinxien(id_zox):
    """ Fonction pour marquer tous les attributs d'un Zoinxien comme déjà vus. """
    x = zoinxiens[id_zox][0]
    y = zoinxiens[id_zox][1]
    tentacule = zoinxiens[id_zox][2]
    age = zoinxiens[id_zox][3]

    deja_vu_x[x].append(id_zox)
    deja_vu_y[y].append(id_zox)
    deja_vu_tentacule[tentacule].append(id_zox)
    marque_age(age, id_zox)

    deja_vu_x[x][0] = 1
    deja_vu_y[y][0] = 1
    deja_vu_tentacule[tentacule][0] = 1
    marque_age(age, id_zox)
    deja_vu[id_zox] = 1

def est_ami(id_zox):
    """ Fonction pour savoir si un Zoinxien est ami, selon les données actuelles. """
    x = zoinxiens[id_zox][0]
    y = zoinxiens[id_zox][1]
    tentacule = zoinxiens[id_zox][2]
    age = zoinxiens[id_zox][3]

    if deja_vu_x[x][0] or deja_vu_y[y][0] or deja_vu_tentacule[tentacule][0] or deja_vu_age[age][0]:
        return True
    else:
        return False

def rajoute_amis(id_zox):
    """ Rajoute les amis d'un zoinxien à la file de parcours. """
    x = zoinxiens[id_zox][0]
    y = zoinxiens[id_zox][1]
    tentacule = zoinxiens[id_zox][2]
    age = zoinxiens[id_zox][3]

    for i in deja_vu_x:
        if not deja_vu[i]:
            file.append(i)

    if not deja_vu_y[y]:
        for i in propriete_y:
            if not deja_vu[i]:
                file.append(i)

    if not deja_vu_tentacule[tentacule]:
        for i in propriete_tentacule:
            if not deja_vu[i]:
                file.append(i)

    if not deja_vu_age[age]:
        for i in propriete_age:
            if not deja_vu[age]:
                file.append(i)


## ---------- Entrées ----------
n = int(input())

for i in range(n):
    zoinxiens[i] = array("i", (map(int, sys.stdin.readline().split())))

    propriete_x[zoinxiens[i][0]].append(i)
    propriete_y[zoinxiens[i][1]].append(i)
    propriete_tentacule[zoinxiens[i][2]].append(i)
    marque_age(zoinxiens[i][3], i)


## ---------- Code ----------
deja_vu_zoinxien(0)
nb_amis = 0

file = deque([0])

while file:
    id_zox = file.popleft()

    x = zoinxiens[id_zox][0]
    y = zoinxiens[id_zox][1]
    tentacule = zoinxiens[id_zox][2]
    age = zoinxiens[id_zox][3]

    if est_ami(id_zox):
        rajoute_amis(id_zox)
        deja_vu_zoinxien(id_zox)
        nb_amis += 1


print(nb_amis)

