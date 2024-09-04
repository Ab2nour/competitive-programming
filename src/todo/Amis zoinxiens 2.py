def main():
    import sys


    ## ---------- Données ----------
    from queue import PriorityQueue
    from array import array


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
        zoinxiens[i] = array("i", (map(int,sys.stdin.readline().split())))


    ## --- File de priorité ---
    file = PriorityQueue()

    # pour les x
    for i in range(n):
        ecart = abs(zoinxiens[0][0] - zoinxiens[i][0]) # clé de la file de priorité
        file.put((ecart, i))

    # pour les y
    for i in range(n):
        ecart = abs(zoinxiens[0][1] - zoinxiens[i][1]) # clé de la file de priorité
        file.put((ecart, i))

    # pour les tentacules
    for i in range(n):
        ecart = abs(zoinxiens[0][2] - zoinxiens[i][2]) # clé de la file de priorité
        file.put((ecart, i))

    # pour les âges
    for i in range(n):
        ecart = abs(zoinxiens[0][3] - zoinxiens[i][3]) # clé de la file de priorité
        file.put((ecart, i))


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


    while not file.empty():
        id_zox = file.get()[1]

        x = zoinxiens[id_zox][0]
        y = zoinxiens[id_zox][1]
        tentacule = zoinxiens[id_zox][2]
        age = zoinxiens[id_zox][3]

        if not deja_vu[id_zox]:
            if est_ami(id_zox):
                #print(zox[4])
                deja_vu_zoinxien(id_zox)
                nb_amis += 1


    print(nb_amis)


main()