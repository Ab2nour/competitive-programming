from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# trois points A, B, C
# on fait le projeté H de A sur la droite (BC)
# aire d'un triangle = (Base x Hauteur) / 2
# donc Aire = BC x AH / 2
# on veut le double donc on renvoie BC x AH

vect = lambda x, y: (y[0] - x[0], y[1] - x[1])
prod_sca = lambda x, y: x[0] * y[0] + x[1] * y[1]
# calculer le vecteur AB et BC

# soit H le projeté d'un point A sur BC
# BH est orienté (mesure algébrique) => valeur absolue
# BH = produit_scalaire(BA, BC)/BC
# grâce à BH, on calcule les coordonnées de H
# on calcule ensuite AH


a = (20, 0)
b = (35, 48)
c = (44, 11)

a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))

v_AB = vect(a, b)
v_BC = vect(b, c)

AB = distance(b[0], b[1], a[0], a[1])
AC = distance(a[0], a[1], c[0], c[1])
BC = distance(b[0], b[1], c[0], c[1])

if BC == 0:
    BC = 0.0000001

BH = prod_sca(v_AB, v_BC) / BC
BH = abs(BH)
coeff = BH / BC

v_BH = (coeff * v_BC[0], coeff * v_BC[1])  # v_BH = coeff*v_BC

h = (b[0] + v_BH[0], b[1] + v_BH[1])

AH = distance(a[0], a[1], h[0], h[1])

# print(int(AH*BC))

abc = AB + AC + BC

g = abc / 2

calcul_intermediaire = g * (g - AB) * (g - AC) * (g - BC)

calcul_intermediaire = abs(calcul_intermediaire)

res = 2 * sqrt(calcul_intermediaire)

print(round(res))

# idée
# calculer BH et HC
# ensuite, on calcule le pourcentage auquel H est de [BC] (peut être supérieur à 100
#   ou inférieur à 0 si à l'extérieur)
# ensuite on calcule le vecteur colinéaire
