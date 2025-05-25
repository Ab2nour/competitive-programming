def main():
    import sys

    readline = sys.stdin.readline
    write = sys.stdout.write

    nb_distributeurs = int(readline())
    nb_operations = int(readline())

    files = [[] for i in range(nb_distributeurs + 1)]

    for i in range(nb_operations):
        num_distribteur, qtite, date = map(int, readline().split())

        if qtite < 0:
            a_enlever = -qtite
            popleft = files[num_distribteur].pop

            while a_enlever > 0:  # faire while a_enlever > tete_file etc
                tete_file = files[num_distribteur][0][1]
                nb_a_enlever = 0  # nb éléments à enlever pour slice !

                if not tete_file <= a_enlever:
                    files[num_distribteur][0][1] -= a_enlever
                    break
                else:
                    while tete_file <= a_enlever:
                        nb_a_enlever += 1
                        a_enlever -= tete_file

                        if nb_a_enlever >= len(files[num_distribteur]):
                            break

                        tete_file = files[num_distribteur][nb_a_enlever][1]

                    files[num_distribteur] = files[num_distribteur][nb_a_enlever:]

        else:
            files[num_distribteur].append([date, qtite])

    for i in range(1, len(files)):
        minimum = 100000000

        for j in range(len(files[i])):  # todo décommenter la ligne dessous !   v
            tete_file = files[i][j][0]
            if tete_file < minimum:  # and files[i][j] > 0:              (ici)
                minimum = tete_file  # l'indice zéro c'est la date

        if minimum == 100000000:
            write("%d\n" % 0)
        else:
            write("%d\n" % minimum)


main()
