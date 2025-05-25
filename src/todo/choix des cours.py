import sys

sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
tab = [0 for j in range(K)]

seuil = N - K + 1


def generateur_noms(K, index):
    if index == K:
        for i in tab:
            sys.stdout.write("%s " % i)
        sys.stdout.write("\n")
        return 0

    if index > 0:
        for i in range(tab[index - 1] + 1, N + 1):
            if (i > seuil and index >= i - seuil) or i <= seuil:
                tab[index] = i
                generateur_noms(K, index + 1)

    else:
        for i in range(1, N + 1):
            tab[index] = i
            generateur_noms(K, index + 1)


if N < K:
    pass
else:
    generateur_noms(K, 0)
