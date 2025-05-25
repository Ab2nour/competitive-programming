def main():
    from collections import deque
    import sys

    readline = sys.stdin.readline
    write = sys.stdout.write

    nb_distributeurs = int(readline())
    nb_operations = int(readline())

    files = [deque() for i in range(nb_distributeurs + 1)]

    for i in range(nb_operations):
        num_distribteur, qtite, date = map(int, readline().split())

        if qtite < 0:
            a_enlever = -qtite
            popleft = files[num_distribteur].popleft

            while a_enlever > 0:
                tete_file = files[num_distribteur][0][1]
                if tete_file <= a_enlever:
                    popleft()
                    a_enlever -= tete_file
                else:
                    files[num_distribteur][0][1] -= a_enlever
                    break

        else:
            files[num_distribteur].append([date, qtite])

    for i in range(1, len(files)):
        minimum = 100000000

        popleft = files[i].popleft
        for j in range(len(files[i])):  # todo décommenter la ligne dessous !   v
            tete_file = popleft()[0]
            if tete_file < minimum:  # and files[i][j] > 0:              (ici)
                minimum = tete_file  # l'indice zéro c'est la date

        if minimum == 100000000:
            write("%d\n" % 0)
        else:
            write("%d\n" % minimum)


main()
