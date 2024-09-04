import sys
from math import sqrt

def distance_tour(x1, y1, x2, y2):
    return (x2-x1)**2+(y2-y1)**2
    #return sqrt((x2-x1)**2+(y2-y1)**2)

x_tour, y_tour = map(int, input().split())

def distance(x, y):
    global x_tour, y_tour
    return distance_tour(x_tour, y_tour, x, y)

N = int(input())

x_min, y_min = map(int, input().split()) # le minimum est le 1er point par défaut

distance_min = distance(x_min, y_min)

for i in range(N-1):
    x, y = map(int, sys.stdin.readline().split())

    dist = distance(x, y)
    if dist < distance_min:
        distance_min = dist
        x_min = x
        y_min = y

print(x_min, y_min)
