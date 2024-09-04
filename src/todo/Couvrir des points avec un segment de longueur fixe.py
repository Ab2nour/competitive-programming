dureeMax, nbEmissions = map(int, input().split())

emissions = list(map(int, input().split()))
emissions.sort()

intervalleMin = 0 # sera incrémenté si on trouve mieux, variable qui stocke le max
                    # ex : si on a trouvé un intervalle qui marche de longueur 3,
                    # on ne teste plus que les intervalles de longueur 4

i = 0
while i + intervalleMin < nbEmissions:
    while i + intervalleMin < nbEmissions and emissions[i+intervalleMin] - emissions[i] <= dureeMax:
        intervalleMin += 1
    i += 1

print(intervalleMin)