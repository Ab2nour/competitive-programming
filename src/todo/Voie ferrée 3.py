import sys
from math import sqrt


def distance(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


x_a, y_a, x_b, y_b = map(int, input().split())

A = (x_a, y_a)
B = (x_b, y_b)


# point A, et B
# coeff a et b
# ax + by + c = 0
def coeff_droite(x1, y1, x2, y2):
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return (a, b)


if x_a == x_b:
    a = 1
    b = 0
    c = -x_a
else:
    b = -1
    a, c = coeff_droite(x_a, y_a, x_b, y_b)


def distance_droite(x, y):
    global a, b, c
    return abs(a * x + b * y + c) / sqrt(a**2 + b**2)


nb_point = int(input())

max = 0
x_max, y_max = x_a, y_a


for _, description in zip(range(nb_point), sys.stdin):
    x, y = map(int, description.split())

    dist = distance_droite(x, y)

    if dist > max:
        max = dist
        x_max, y_max = x, y


print(x_max, y_max)
