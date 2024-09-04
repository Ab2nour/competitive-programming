nb_distributeurs = int(input())
nb_operations = int(input())



files = [[0 for i in range(1000)] for i in range(nb_distributeurs+1)]
indice_debut = [0 for i in range(nb_distributeurs+1)]
indice_fin = [0 for i in range(nb_distributeurs+1)]

for i in range(nb_operations):
    num_distribteur, qtite, date = map(int, input().split())

    if qtite > 0:
        for j in range(qtite):
            files[num_distribteur][indice_fin[num_distribteur]%1000] = date
            indice_fin[num_distribteur] += 1
    else:
        for j in range(-qtite):
            files[num_distribteur][indice_debut[num_distribteur]%1000] = 0
            indice_debut[num_distribteur] += 1

for i in range(1, len(files)):
    minimum = 100000000
    for j in range(indice_debut[i], indice_fin[i]):
        if files[i][j] < minimum and files[i][j] > 0:
            minimum = files[i][j]

    if minimum == 100000000:
        print(0)
    else:
        print(minimum)