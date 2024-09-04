from sys import stdin, stdout


input = stdin.readline
print = stdout.write

# -------------------- dico --------------------
D = int(input())
dico = ['' for i in range(D)]

for i in range(D):
    dico[i] = input()[:-1]


# -------------------- lettres --------------------
N = int(input())
lettres = ['' for i in range(N)]

for i in range(N):
    lettres[i] = input()[:-1]


# -------------------- code --------------------
test = False
iterateur = 0
nb_lettres_correctes = 0

while not test:
    if len(dico[iterateur]) == N: # le bon nombre de lettres
        while (nb_lettres_correctes < N) and (dico[iterateur][nb_lettres_correctes] in lettres[nb_lettres_correctes]):
            # nb_lettres_correctes sert à la fois de compteur pour le test
            #   et aussi d'itérateur
            nb_lettres_correctes += 1
    if nb_lettres_correctes == N:
        print(dico[iterateur])
        break
    nb_lettres_correctes = 0
    iterateur += 1

