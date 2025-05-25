def dichotomie(liste, valeur, debut, fin):
    if debut == fin:
        return valeur == liste[debut]

    milieu = (debut + fin) // 2

    if valeur == liste[milieu]:
        return True

    elif valeur <= liste[milieu]:
        return dichotomie(liste, valeur, debut, milieu)

    else:
        return dichotomie(liste, valeur, milieu + 1, fin)


n, valeur_cible = map(int, input().split())

peintures = list(map(int, input().split()))

for i in peintures:
    if i > valeur_cible:
        print("NON")
        exit()
    if dichotomie(peintures, valeur_cible - i, 0, n - 1):
        print("OUI")
        exit()

print("NON")
