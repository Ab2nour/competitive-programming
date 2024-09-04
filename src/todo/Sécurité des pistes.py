## croisement (résolution équation)
## on cherche x
# ax + b = y
# mx + p = y

# ax + b = mx + p
# ax - mx = p - b
# (a-m)x = p-b
# x = (p-b)/(a-m)

## on cherche y
# ax + b = y
# y = a*x + b

def croisement(a, b, m, p):
    x = (p-b)/(a-m)
    y = a*x + b
    return (x, y)

def coeff_droite(x1, y1, x2, y2):
    if x1 == x2:
        x1 += 0.000001
    a = (y1-y2)/(x1-x2)
    b = y1 - a*x1
    return (a, b)


x1, y1, x2, y2 = map(int, input().split())
a, b = coeff_droite(x1, y1, x2, y2)

x1, y1, x2, y2 = map(int, input().split())
m, p = coeff_droite(x1, y1, x2, y2)

x, y = croisement(a, b, m, p)

print(x, y)
## calculer ax+b à partir de 2 points (x1, y1) et (x2, y2)
## on cherche a
# a*x1 + b = y1
# a*x2 + b = y2

# b = y1 - a*x1
# b = y2 - a*x2

# y1 - a*x1 = y2 - a*x2
# y1 - y2 =  a*x1 - a*x2
# y1 - y2 = (x1-x2)*a
# a = (y1-y2)/(x1-x2)

## on cherche b
# a*x1 + b = y1
# b = y1 - a*x1