## ---------- Entrées ----------
entree = """0 0 42 10
0 2 3 1
2 2 5 21
1 1 4 15
3 3 2 50
4 4 3 40"""

entree = entree.split("\n")


## ---------- Données ----------
from queue import PriorityQueue

MAX_ZOINXIEN = 200  # 000
n = 6

deja_vu_x = [0 for i in range(MAX_ZOINXIEN)]
deja_vu_y = [0 for i in range(MAX_ZOINXIEN)]
deja_vu_tentacule = [0 for i in range(MAX_ZOINXIEN)]
deja_vu_age = [0 for i in range(MAX_ZOINXIEN)]

deja_vu = [0 for i in range(MAX_ZOINXIEN)]

zoinxiens = [0 for i in range(MAX_ZOINXIEN)]
for i in range(n):
    zoinxiens[i] = list(map(int, entree[i].split()))

## --- File de priorité ---
file = PriorityQueue()

# pour les x
for i in range(n):
    ecart = abs(zoinxiens[0][0] - zoinxiens[i][0])  # clé de la file de priorité
    x = zoinxiens[i][0]
    y = zoinxiens[i][1]
    tentacule = zoinxiens[i][2]
    age = zoinxiens[i][3]

    file.put((ecart, x, y, tentacule, age, i))

# pour les y
for i in range(n):
    ecart = abs(zoinxiens[0][1] - zoinxiens[i][1])  # clé de la file de priorité
    x = zoinxiens[i][0]
    y = zoinxiens[i][1]
    tentacule = zoinxiens[i][2]
    age = zoinxiens[i][3]

    file.put((ecart, x, y, tentacule, age, i))

# pour les tentacules
for i in range(n):
    ecart = abs(zoinxiens[0][2] - zoinxiens[i][2])  # clé de la file de priorité
    x = zoinxiens[i][0]
    y = zoinxiens[i][1]
    tentacule = zoinxiens[i][2]
    age = zoinxiens[i][3]

    file.put((ecart, x, y, tentacule, age, i))

# pour les âges
for i in range(n):
    ecart = abs(zoinxiens[0][3] - zoinxiens[i][3])  # clé de la file de priorité
    x = zoinxiens[i][0]
    y = zoinxiens[i][1]
    tentacule = zoinxiens[i][2]
    age = zoinxiens[i][3]

    file.put((ecart, x, y, tentacule, age, i))

# # --- Quatre listes triées selon x, y, tentacule et âge ---
# zox_x = zoinxiens[:]
# zox_y = zoinxiens[:]
# zox_tentacule = zoinxiens[:]
# zox_age = zoinxiens[:]
#
# zox_x.sort(key = lambda x : abs(zoinxiens[0][0] - x[0]))
# zox_y.sort(key = lambda x : abs(zoinxiens[0][1] - x[1]))
# zox_tentacule.sort(key = lambda x : abs(zoinxiens[0][2] - x[2]))
# zox_age.sort(key = lambda x : abs(zoinxiens[0][3] - x[3]))


## ---------- Fonctions ----------
def marque_age(n):
    """Fonction pour marquer les cases adjacentes à l'âge (plus ou moins 5 ans)."""
    if n < 5:
        for i in range(0, (n + 1) + 5):
            deja_vu_age[i] = 1

    elif n > MAX_ZOINXIEN - 5:
        for i in range(n - 5, MAX_ZOINXIEN + 1):
            deja_vu_age[i] = 1

    else:
        for i in range(n - 5, (n + 1) + 5):
            deja_vu_age[i] = 1


def deja_vu_zoinxien(zox):
    """Fonction pour marquer tous les attributs d'un Zoinxien comme déjà vus."""
    x = zox[0]
    y = zox[1]
    tentacule = zox[2]
    age = zox[3]
    identifiant = zox[4]

    deja_vu_x[x] = 1
    deja_vu_y[y] = 1
    deja_vu_tentacule[tentacule] = 1
    marque_age(age)
    deja_vu[identifiant] = 1


def est_ami(zox):
    """Fonction pour savoir si un Zoinxien est ami, selon les données actuelles."""
    x = zox[0]
    y = zox[1]
    tentacule = zox[2]
    age = zox[3]

    if deja_vu_x[x] or deja_vu_y[y] or deja_vu_tentacule[tentacule] or deja_vu_age[age]:
        return True
    else:
        return False


## ---------- Code ----------
deja_vu_zoinxien(zoinxiens[0] + [0])
nb_amis = 0


while not file.empty():
    zox = file.get()
    zox = zox[1:]

    if not deja_vu[zox[4]]:
        if est_ami(zox):
            print(zox[4])
            deja_vu_zoinxien(zox)
            nb_amis += 1


print(nb_amis)
