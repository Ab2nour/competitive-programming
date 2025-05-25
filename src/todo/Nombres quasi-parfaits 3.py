from math import sqrt

l = int(input())
d = int(input())

MAX_L = 1000000 + 1

s = [1 for i in range(MAX_L)]
s[0] = 0
s[1] = 0

limite = int(sqrt(MAX_L)) + 1
for i in range(2, limite):
    for j in range(i + 1, limite):
        s[i * j] += i + j

# Cela crée des surplus au niveau des carrés
# ex : s[9] = s[3x3] va être incrémenté de "3 + 3" car i = j
for i in range(2, limite):
    s[i**2] += i


compteur = 0

for i in range(1, l + 1):
    if abs(s[i] - i) <= d:
        compteur += 1

print(compteur)
