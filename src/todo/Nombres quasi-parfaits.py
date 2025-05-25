from math import sqrt

l = int(input())
d = int(input())

MAX_L = 1000000 + 1

tab_s = [0 for i in range(MAX_L)]


def s(n):
    """Formule générale :

    Supposons que n s'écrive sous forme : k * p
    Avec k et p entiers, p étant un nombre premier

    Alors :
    S(k*p) = (S(k) – 1) * p + S(k)
           = p*S(k) - p + S(k)
           = (p+1)*S(k) - p
    """
    if tab_s[n] != 0:
        return tab_s[n]

    elif n % 2 == 0:
        tab_s[n] = 3 + moitie  # 1 + 2 + n//2

    elif n % 3 == 0 and tab_s[tiers] == 1:
        tab_s[n] = 4 + tiers  # 1 + 3 + n//2

    elif tab_s[n] == 0:
        compteur = 0
        # limite = int(sqrt(n)) + 1
        limite = n // 2 + 1

        for i in range(1, limite):
            if n % i == 0:
                compteur += i

        tab_s[n] = compteur

    return tab_s[n]


## Initialisation
compteur = 0
# s[]

for i in range(2, l + 1):
    resultat = s(i)

    if abs(resultat - i) <= d:
        compteur += 1

print(compteur)
