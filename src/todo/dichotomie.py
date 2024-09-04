from math import log, ceil

def dichotomie(some_list, value):
    n = len(some_list)//2
    n_original = n
    print(n)

    nb_etapes = ceil(log(n, 2))

    for i in range(nb_etapes):
        if some_list[n] == value:
            return n
        elif some_list[n] < value:
            n += n_original//(2**(i+1))
            print(n)
        else:
            n -= n_original//(2**(i+1))
            print(n)

    #while n
    print("----------")
    return n

def dichotomie(some_list, value, taille_segment):
    if taille_segment == 1:
        return 0
    n = taille_segment//2


def valeur_plus_proche(some_list, value):
    # on compare la valeur trouvée avec ses deux voisins
    n = dichotomie(some_list, value, len(some_list))

    minimum = some_list[n] - value


    if abs(some_list[n-1] - value) < abs(minimum):
        minimum = some_list[n-1] - value
    if (n+1) < len(some_list) and abs(some_list[n+1] - value) < abs(minimum):
        minimum = some_list[n-1] - value

    return value + minimum



test = "41 32 11 17 24 8 16"

test = list(map(int, test.split()))

test.sort()

