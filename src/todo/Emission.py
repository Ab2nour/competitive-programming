nbEmissions, dureeMax = map(int, input().split())

emissions = list(map(int, input().split()))

tab_cumulatif = [0 for i in range(nbEmissions+1)]

#tab_cumulatif[0] = emissions[0]

for i in range(1, nbEmissions+1):
    tab_cumulatif[i] = emissions[i-1] + tab_cumulatif[i-1]

intervalleMin = 0 # sera incrémenté si on trouve mieux, variable qui stocke le max
                    # ex : si on a trouvé un intervalle qui marche de longueur 3,
                    # on ne teste plus que les intervalles de longueur 4

valeur_max = 0

i = 0
while i + intervalleMin <= nbEmissions-1:
    while i +intervalleMin <= nbEmissions-1 and tab_cumulatif[i+intervalleMin+1] - tab_cumulatif[i] <= dureeMax:
        intervalleMin += 1
    i += 1


print(intervalleMin)