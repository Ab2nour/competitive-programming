N = int(input())

a = 1

for i in range(N):
    a *= int(input()) % 1000

a = a % 1000

print("{:04d}".format(a))
