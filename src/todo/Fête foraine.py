import sys

## Variables
nb_cibles = int(sys.stdin.readline())
gain_cibles = list(map(int, sys.stdin.readline().split()))

nb_lots = int(sys.stdin.readline())
valeur_lots = list(map(int, sys.stdin.readline().split()))
valeur_lots = [0] + valeur_lots

index_meilleur_lot = 0

## Programme
for i in range(nb_cibles):
    cible_actuelle = gain_cibles[i]

    while (
        index_meilleur_lot <= nb_lots
        and cible_actuelle >= valeur_lots[index_meilleur_lot]
    ):
        index_meilleur_lot += 1

    sys.stdout.write("%d " % valeur_lots[index_meilleur_lot - 1])
