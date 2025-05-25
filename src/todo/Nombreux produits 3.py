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
            popleft = files[num_distribteur].popleft
            for j in range(-qtite):
                popleft()
        else:
            append = files[num_distribteur].append
            for j in range(qtite):
                append(date)

    for i in range(1, len(files)):
        minimum = 100000000

        for j in range(len(files[i])):
            if files[i][j] < minimum:  # and files[i][j] > 0:
                minimum = files[i][j]

        if minimum == 100000000:
            write("%d\n" % 0)
        else:
            write("%d\n" % minimum)


main()
