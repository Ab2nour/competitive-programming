S = int(input())

# spectacles = [
#     (900, 250),
#     (600, 200),
#     (3600, 50),
#     (800, 400),
#     (7200, 20),
#     (2400, 360)
# ]

spectacles = [0 for i in range(S)]

for i in range(S):
    spectacles[i] = tuple(map(int, input().split()))

spectacles.sort()

tab_somme = [0 for i in range(S)]
tab_somme[0] = spectacles[0][1]
for i in range(1, S):
    tab_somme[i] = tab_somme[i-1] + spectacles[i][1]


somme_jusqua_n = lambda n : tab_somme[n-1]/n

tab_moyennes = [somme_jusqua_n(i+1) for i in range(S)]

max = tab_moyennes[0]
indice_max = 0

for i in range(S):
    if tab_moyennes[i] >= max:
        max = tab_moyennes[i]
        indice_max = i

print(spectacles[indice_max][0])