N = int(input())

tablo = [0 for i in range(N)]

entiers = list(map(int, input().split()))

entiers.sort()

distance_min = 2*(10**8) + 1

for i in range(N-1):
    distance_actuelle = entiers[i+1] - entiers[i]
    if  distance_actuelle < distance_min:
        distance_min = distance_actuelle

print(distance_min)