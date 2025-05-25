from queue import PriorityQueue


### Entrées
nbPieces = int(input())

nbMachinesA = int(input())
machinesA = [int(temps) for temps in input().split()]

nbMachinesB = int(input())
machinesB = [int(temps) for temps in input().split()]


### Fonctions
def tempsMinSansDelai(nbPieces, machines):
    enAttente = PriorityQueue()

    for temps in machines:
        enAttente.put((temps, temps))

    temps = []

    for _ in range(nbPieces):
        tempsMin, tempsTraitement = enAttente.get()
        temps.append(tempsMin)
        enAttente.put((tempsMin + tempsTraitement, tempsTraitement))

    return temps


def tempsMin(delais, machines):
    enAttente = PriorityQueue()

    for temps in machines:
        enAttente.put((temps, temps))

    tempsMinTotal = 0

    for tempsArrivee in reversed(delais):
        tempsMin, tempsTraitement = enAttente.get()
        tempsMinTotal = max(tempsMinTotal, tempsMin + tempsArrivee)
        enAttente.put((tempsMin + tempsTraitement, tempsTraitement))

    return tempsMinTotal


### Programme
tempsA = tempsMinSansDelai(nbPieces, machinesA)
tempsMinA = tempsA[len(tempsA) - 1]

tempsMinB = tempsMin(tempsA, machinesB)


### Affichage
print(tempsMinA)
print(tempsMinB)
