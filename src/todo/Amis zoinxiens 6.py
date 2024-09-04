def main():
    import sys

    ## ---------- Données ----------
    from array import array
    from collections import deque


    MAX_ZOINXIEN = 200000

    deja_vu_x = array("b", [0 for i in range(MAX_ZOINXIEN+1)])
    deja_vu_y = array("b", [0 for i in range(MAX_ZOINXIEN+1)])
    deja_vu_tentacule = array("b", [0 for i in range(MAX_ZOINXIEN+1)])
    deja_vu_age = array("b", [0 for i in range(MAX_ZOINXIEN+1)])

    deja_vu = array("b", [0 for i in range(MAX_ZOINXIEN+1)])

    zoinxiens = [0 for i in range(MAX_ZOINXIEN)]


    ## ---------- Entrées ----------
    n = int(input())

    for i in range(n):
        zoinxiens[i] = array("i", (map(int, sys.stdin.readline().split())))


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



    ## ---------- Code ----------
    deja_vu_zoinxien(0)
    nb_amis = 0
    nouveaux_amis_trouves = True
    file = deque(range(1, n))

    while file and nouveaux_amis_trouves:
        #print("ok roger 1 :", file)
        nouveaux_amis_trouves = False

        for i in range(len(file)):
            id_zox = file.popleft()

            x = zoinxiens[id_zox][0]
            y = zoinxiens[id_zox][1]
            tentacule = zoinxiens[id_zox][2]
            age = zoinxiens[id_zox][3]

            if est_ami(id_zox):
                nouveaux_amis_trouves = True
                deja_vu_zoinxien(id_zox)
                nb_amis += 1
            else:
                file.append(id_zox)

        #print("ok roger 2 :", file)

    print(nb_amis)

main()