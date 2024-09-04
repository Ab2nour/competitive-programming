N = int(input())
P = int(input())

factorial = [i for i in range(13)]
factorial[0] = 1

for i in range(3, 13):
    factorial[i] = factorial[i] * factorial[i-1]

fact = lambda n : factorial[n]

def combi(n, k): # k parmi n
    return int(fact(n)/(fact(k)*fact(n-k)))

print(combi(N, P))