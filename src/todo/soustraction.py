base, N1, N2 = map(int, input().split())

max_taille = max(N1, N2)+1

retenues = [0 for i in range(max_taille)]

resultat = [0 for i in range(max_taille)]

nb1 = list(map(int, input().split()))
nb2 = list(map(int, input().split()))

negatif = False

# on intervertit les deux si nb2 est plus grand
if N2 > N1:
    nb1, nb2 = nb2, nb1
    negatif = True

if N2 == N1:
    for i in range(N1):
        if nb2[i] > nb1[i]:
            nb1, nb2 = nb2, nb1
            negatif = True
            break
        elif nb2[i] < nb1[i]:
            break



# rajout de zéros pour la bonne taille
nb1 = [0 for i in range(max_taille-len(nb1))] + nb1
nb2 = [0 for i in range(max_taille-len(nb2))] + nb2

# calcul
for i in range(1, max_taille):
    if nb1[-i] >= nb2[-i]:
        soustraction = nb1[-i] - nb2[-i] + retenues[-i]
    else:
        soustraction = nb1[-i] + base - nb2[-i] + retenues[-i]
        retenues[-i-1] -= 1

    if soustraction < 0:
        resultat[-i] = base + soustraction
        retenues[-i-1] -= 1
    else:
        resultat[-i] = soustraction

# cas où le nombre est négatif
if negatif:
    print("-", end=" ")

# si le 1er chiffre est un zéro on ne l'affiche pas
# (attention au résultat nul (égal à zéro) )
compteur = 0
while resultat[compteur] == 0 and compteur < len(resultat)-1:
    compteur += 1

for i in range(compteur, len(resultat)):
    print(resultat[i], end=" ")

