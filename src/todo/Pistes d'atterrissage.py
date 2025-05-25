from math import sqrt
import sys


def coeff_droite(x1, y1, x2, y2):
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return (a, b)


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    # soit H le projeté d'un point P sur AB
    # AH est orienté (mesure algébrique)
    # AH = produit_scalaire(AP, AB)/AB

    vect = lambda x, y: (y[0] - x[0], y[1] - x[1])
    prod_sca = lambda x, y: x[0] * y[0] + x[1] * y[1]

    # x_a, y_a, x_b, y_b = map(int, input().split())
    x, y = map(int, input().split())

    nb_point = int(input())

    valeur_min = 10**10 + 1
    x_a_min, y_a_min, x_b_min, y_b_min = 0, 0, 0, 0

    # for _,description in zip(range(nb_point), sys.stdin):
    for i in range(nb_point):
        x_a, y_a, x_b, y_b = map(int, sys.stdin.readline().split())

        A = (x_a, y_a)
        B = (x_b, y_b)

        AB = vect(A, B)
        dist_ab = distance(x_a, y_a, x_b, y_b)

        resultat = prod_sca(AB, vect(A, (x, y))) / dist_ab  # distance AH

        # fonction ici
        if resultat <= 0:
            print("C1")
            valeur = distance(x, y, x_a, y_a)
        elif resultat < dist_ab:
            print("C2")
            if x_a == x_b:
                a = 1
                b = 0
                c = -x_a
            else:
                b = -1
                a, c = coeff_droite(x_a, y_a, x_b, y_b)

            valeur = abs(a * x + b * y + c) / sqrt(a**2 + b**2)
        else:
            print("C3")
            valeur = distance(x, y, x_b, y_b)

        print("valeur", valeur, "valeur min", valeur_min)
        if valeur < valeur_min:
            valeur_min = valeur
            x_a_min, y_a_min, x_b_min, y_b_min = x_a, y_a, x_b, y_b

    print(x_a_min, y_a_min, x_b_min, y_b_min)


main()
