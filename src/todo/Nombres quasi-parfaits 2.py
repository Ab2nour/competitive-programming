from math import sqrt

l = int(input())
d = int(input())

MAX_L = 1000000+1

#tab_s = [0 for i in range(MAX_L)]

def s(n):
    # Renvoie True si la fonction s'est terminée
    # et False si on ne respecte pas "abs(s(n) - n) <= d"
    compteur = 0
    #limite = int(sqrt(n)) + 1
    limite = n // 2 + 1
    #todo remettre limite à sqrt(n) !

    print("s(" + str(n) + ")")

    i = 1
    while i < limite:
        print("compteur", compteur, "n", n)
        print(abs(compteur - n))
        if abs(compteur - n) <= d:
            if n % i == 0:
                compteur += i

            i += 1
        else:
            return False

    return True





compteur_global = 0

for i in range(1, l+1):
    resultat = s(i)
    if resultat:
        compteur_global += 1

print(compteur_global)