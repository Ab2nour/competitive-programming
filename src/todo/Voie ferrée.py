# soit un point P et un segment [AB]
# on projette P sur AB, cela donne le point H
# on calcule AH comme ceci :
# AH = prod_sca(AB, AP)/AB
# AH = abs(AH)

# on se place dans le triangle rectangle APH, rectangle en H
# AP² = AH² + PH²
# PH² = AP²-AH²

# on a trouvé la distance, donc PH (au carré ça ne change pas les comparaisons)

# PH² = AP² - AH²
# PH² = AP² - abs(prod_sca(AB, AP)/dist_ab)**2
# dist = distance(x_a, y_a, x, y)**2 - abs(prod_sca(AB, AP)/dist_ab)**2

import sys


def distance(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


vect = lambda x, y: (y[0] - x[0], y[1] - x[1])
prod_sca = lambda x, y: x[0] * y[0] + x[1] * y[1]

x_a, y_a, x_b, y_b = map(int, input().split())

a = (x_a, y_a)
b = (x_b, y_b)

AB = vect(a, b)
dist_ab = distance(x_a, y_a, x_b, y_b)

nb_point = int(input())

max = 0
x_max, y_max = x_a, y_a


def distance_tour(x, y):
    AP = vect(a, (x, y))
    AH = prod_sca(AB, AP) / dist_ab
    dist_AP = distance(x_a, y_a, x, y)
    print("AP", dist_AP)
    print("AH", AH)

    dist = dist_AP**2 - AH**2

    return dist


for _, description in zip(range(nb_point), sys.stdin):
    x, y = map(int, description.split())

    AP = vect(a, (x, y))
    AH = prod_sca(AB, AP) / dist_ab
    dist_AP = distance(x_a, y_a, x, y)

    dist = dist_AP**2 - AH**2

    if dist > max:
        max = dist
        x_max, y_max = x, y


print(x_max, y_max)
