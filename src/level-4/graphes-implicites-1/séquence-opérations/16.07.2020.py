a, b, c, d = map(int, input().split())
n, m = map(int, input().split())
deja_visite = [0 for i in range(10**5+1)]
file = [n]
while file:
    nombre = file.pop(0)
    resultat = nombre + a
    if resultat <= 10**5:
        if resultat == m:
            print(1)
            exit()
        elif deja_visite[resultat] == 0:
            deja_visite[resultat] = 1
            file.append(resultat)
    resultat = nombre - b
    if resultat >= 0:
        if resultat == m:
            print(1)
            exit()
        elif deja_visite[resultat] == 0:
            deja_visite[resultat] = 1
            file.append(resultat)
    resultat = nombre * c
    if resultat <= 10**5:
        if resultat == m:
            print(1)
            exit()
        elif deja_visite[resultat] == 0:
            deja_visite[resultat] = 1
            file.append(resultat)
    if d != 0:
        resultat = nombre / d
        if isinstance(resultat, int): # resultat entier
            if resultat == m:
                print(1)
                exit()
            elif deja_visite[resultat] == 0:
                deja_visite[resultat] = 1
                file.append(resultat)
print(0)
