# soit H le projeté d'un point P sur AB
# AH est orienté (mesure algébrique)
# AH = produit_scalaire(AP, AB)/AB

from math import sqrt
import sys


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


vect = lambda x, y: (y[0] - x[0], y[1] - x[1])
prod_sca = lambda x, y: x[0] * y[0] + x[1] * y[1]

x_a, y_a, x_b, y_b = map(int, input().split())

a = (x_a, y_a)
b = (x_b, y_b)

AB = vect(a, b)
dist_ab = distance(x_a, y_a, x_b, y_b)

nb_point = int(input())


for _, description in zip(range(nb_point), sys.stdin):
    x, y = map(int, description.split())
    resultat = prod_sca(AB, vect(a, (x, y))) / dist_ab
    sys.stdout.write("%f\n" % (resultat))
