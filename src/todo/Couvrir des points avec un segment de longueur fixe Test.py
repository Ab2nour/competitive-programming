dureeMax, nbEmissions = map(int, "4 9".split())

emissions = list(map(int, "1 2 3 8 9 13 15 16 18".split()))
emissions = list(map(int, "1 4 6 8 9 13 15 16 18".split()))

### Copier en-dessous
intervalleMin = 0 # sera incrémenté si on trouve mieux, variable qui stocke le max
                    # ex : si on a trouvé un intervalle qui marche de longueur 3,
                    # on ne teste plus que les intervalles de longueur 4

i = 0
while i + intervalleMin < nbEmissions:
    print("\n-----------------------------------------")
    print(emissions[i+intervalleMin], "-", emissions[i], "=", emissions[i+intervalleMin] -  emissions[i])
    while emissions[i+intervalleMin] - emissions[i] <= dureeMax:
        print(emissions[i+intervalleMin], "-", emissions[i], "=", emissions[i+intervalleMin] -  emissions[i], "<=", dureeMax)
        intervalleMin += 1
        print("( i", i, "intervalleMin", intervalleMin, ")")
    i += 1

print(intervalleMin-1)