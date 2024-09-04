import sys

c, r = map(int, input().split())

n = int(input())

hauteur_max = [0 for i in range(100)]

def max_3_colonnes(n):
    """ Hauteur minimum des 3 colonnes n, n+1 et n+2. """
    return max(hauteur_max[n], hauteur_max[n+1], hauteur_max[n+2])

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if b > hauteur_max[a-1]:
        hauteur_max[a-1] = b


hauteur = 0

## c < 3
if c < 3:
    if c == 1:
        hauteur = hauteur_max[0]
    elif c == 2:
        hauteur = min(hauteur_max[0], hauteur_max[1])

## c % 3 == 0
elif c % 3 == 0:
    h1, h2, h3 = 0, 0, 0

    for i in range(0, c, 3):
        h1 += max_3_colonnes(i)

    for i in range(1, c-2, 3):
        h2 += max_3_colonnes(i)
    h2 += hauteur_max[0]
    h2 += max(hauteur_max[c-1], hauteur_max[c-2])


    for i in range(2, c-1, 3):
        h3 += max_3_colonnes(i)
    h3 += max(hauteur_max[0], hauteur_max[1])
    h3 += hauteur_max[c-1]

    hauteur = min(h1, h2, h3)
    print(h1, h2, h3)
    print(hauteur_max[:7])

## c % 3 == 1
elif c % 3 == 1:
    h1, h2, h3 = 0, 0, 0

    for i in range(0, c-1, 3):
        h1 += max_3_colonnes(i)
    h1 += hauteur_max[c-1]

    for i in range(1, c, 3):
        h2 += max_3_colonnes(i)
    h2 += hauteur_max[0]

    for i in range(2, c-2, 3):
        h3 += max_3_colonnes(i)
    h3 += max(hauteur_max[0], hauteur_max[1])
    h3 += max(hauteur_max[c-1], hauteur_max[c-2])

    hauteur = min(h1, h2, h3)

## c % 3 == 2
elif c % 3 == 2:
    h1, h2, h3 = 0, 0, 0

    for i in range(0, c-2, 3):
        h1 += max_3_colonnes(i)
    h1 += max(hauteur_max[c-1], hauteur_max[c-2])

    for i in range(1, c-1, 3):
        h2 += max_3_colonnes(i)
    h2 += hauteur_max[0] + hauteur_max[c-1]

    for i in range(2, c, 3):
        h3 += max_3_colonnes(i)
    h3 += max(hauteur_max[0], hauteur_max[1])

    hauteur = min(h1, h2, h3)



print(hauteur)

#todo faire un tableau pour mémoriser tous les max_3_colonnes(i) pour i de 1 à n
#todo faire toutes les permutations des DEUX intervalles autres que les 3
# (33*33 dans le pire des cas il me semble)