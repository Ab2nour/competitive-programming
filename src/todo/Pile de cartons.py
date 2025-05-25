import sys
from array import array

sys.setrecursionlimit(12**8)

nbCartons = int(input())

cartons = [[] for i in range(nbCartons + 1)]

for i in range(nbCartons + 1):
    cartons[i] = array("i", (map(int, sys.stdin.readline().split())))


def parcours(numCarton):
    sys.stdout.write("%s %s\n" % ("A", numCarton))
    for i in range(1, cartons[numCarton][0] + 1):
        parcours(cartons[numCarton][i])
    sys.stdout.write("%s %s\n" % ("R", numCarton))


# pour ne pas afficher "A 0" et "R 0"
for i in range(1, cartons[0][0] + 1):
    parcours(cartons[0][i])
